import csv
import arrow
# import mysql.connector
from base import Base

class NetflixLoader(Base):

    def create_tables(self):
        fd = open('tables.sql', 'r')
        sqlFile = fd.read()
        fd.close()
    
        sqlCommands = sqlFile.split(';')
    
        for command in sqlCommands:
            self.cursor.execute(command)

    def load_csv(self):
        with open('netflix_titles.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    self.load_row(row)
                  
                print(f'Processed {line_count} lines.')
                
    def get_date(self, date):
        try:
            return arrow.get(date, 'MMMM D, YYYY').datetime
        except arrow.parser.ParserMatchError:
            print(f'Error in date.')
            return None
        
    def load_row(self, row):
        show_id = row[0].replace('s', '')
        title = row[2]
        description = row[11]

        type_id = self.insert_dim('type', 'type', row[1])
        date_added = self.get_date(row[6])
        release_year = row[7]
        rating_id = self.insert_dim('rating', 'rating', row[8])
        duration_id = self.insert_dim('duration', 'duration', row[9])

        sql = '''INSERT INTO shows 
        (id, title, description, type_id, date_added, 
         release_year, rating_id, duration_id)
        VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        
        values = (show_id, title, description, type_id, date_added, 
                  release_year, rating_id, duration_id)
        self.cursor.execute(sql, values)
        show_id = self.cursor.lastrowid
        
        directors = self.insert_multi_dim('director', 'name', row[3])
        actors = self.insert_multi_dim('actor', 'name', row[4])
        countries = self.insert_multi_dim('country', 'country', row[5])
        categories = self.insert_multi_dim('category', 'category', row[10])
        self.db.commit()
        
        self.insert_bridge('actor', show_id, actors)
        self.insert_bridge('country', show_id, countries)
        self.insert_bridge('category', show_id, categories)
        self.insert_bridge('director', show_id, directors)
        self.db.commit()
        
        print(f'=={row[0]}==')
        
    def insert_bridge(self, model, show_id, items):
        table = f"{model}_bridge"
        for item_id in items:
            sql = f"INSERT INTO {table} (show_id, {model}_id) VALUES (%s, %s)"
            self.cursor.execute(sql, (show_id, item_id))
            self.db.commit()
    
    def insert_dim(self, model, field, val):
        table = f'{model}_dim'
        sql = f"SELECT id FROM {table} WHERE {field} = %s"
        self.cursor.execute(sql, (val,))
        xid = self.cursor.fetchone()
        
        if xid is None:
            sql = f"INSERT INTO {table} ({field}) VALUES (%s)"
            self.cursor.execute(sql, (val,))
            xid = self.cursor.lastrowid
            self.db.commit()
        else:
            xid = xid[0]

        return xid

    def insert_multi_dim(self, model, field, items):
        item_ids = []
        for item in items.split(','):
            
            value = item.strip()
            sql = f"SELECT id FROM {model}_dim WHERE {field} = %s"
            self.cursor.execute(sql, (value,))
            item = self.cursor.fetchone()
            
            if item is None:
                sql = f"INSERT INTO {model}_dim ({field}) VALUES (%s)"
                self.cursor.execute(sql, (value,))
                item_id = self.cursor.lastrowid
                self.db.commit()
            else:
                item_id = item[0]
                
            item_ids.append(item_id)      
            
        return item_ids
    
if __name__ == '__main__':
    nl = NetflixLoader()
    nl.load_csv()
