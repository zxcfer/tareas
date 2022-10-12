from loaders import NetflixLoader
from reports import Validator, Search
from gender_detector import GenderUpdater
from base import Base


class Search(Base):

    def common_first_name(self, gender_str):
        if gender_str == 'male':
            gender = 1
        else:
            gender = 2
            
        sql = """
        SELECT first_name, count(*) as total FROM (
        SELECT 
            id,
            if( INSTR(`name`, ' ')=0, 
              TRIM(SUBSTRING(`name`, INSTR(`name`, ' ')+1)), 
              TRIM(SUBSTRING(`name`, 1, INSTR(`name`, ' ')-1)) ) AS first_name,
            gender
        FROM actor_dim
        WHERE gender = %s) as T
        GROUP BY first_name
        ORDER BY total DESC
        LIMIT 1
        """
        self.cursor.execute(sql, (gender,))
        return self.cursor.fetchone()[0]

    def longest_timespan(self):
        sql = """
        SELECT id, title, date_added, release_year, 
          DATEDIFF(date_added, CONCAT_WS('-', release_year, 01, 01)) AS timespan
        FROM shows ORDER BY timespan DESC LIMIT 1
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()[1]   

    def month_most_new_releases(self):
        sql = """
        SELECT month_added, count(id) as total FROM (
            SELECT id, MONTH(date_added) month_added FROM shows) AS T
        GROUP BY month_added
        ORDER BY total DESC
        LIMIT 1
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]   
    
    def largest_increase(self):
        self.cursor.execute('set @prev=0;')

        sql = """
        SELECT year_added, curr_total-lag_total as delta FROM (
        SELECT year_added, @prev lag_total, @prev:=total curr_total FROM (
        SELECT year_added, count(id) as total FROM (
            SELECT id, YEAR(date_added) year_added FROM shows 
            WHERE date_added is not null AND type_id = 1) AS T
        GROUP BY year_added
        ORDER BY year_added) as T2) as T3 ORDER BY delta DESC LIMIT 1;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]   
    
    def actresses_woody_harrelson(self):
        sql = """
        SELECT name FROM actor_dim WHERE gender = 2 AND id in (
          SELECT actor_id FROM (
             SELECT actor_id, count(*) as times FROM actor_bridge 
             WHERE show_id IN (
               SELECT show_id FROM actor_bridge WHERE actor_id = (
                 SELECT id 
                 FROM actor_dim
                 WHERE name = 'Woody Harrelson'
               ))
             GROUP BY actor_id 
             ORDER BY times DESC) AS T1
           WHERE times >= 2
        )
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

if __name__ == '__main__':
    #nl = NetflixLoader()
    #nl.create_tables()
    #nl.load_csv()
    
    # gu = GenderUpdater()
    # gu.update_gender()
    
    search = Search()
    print(search.common_first_name('male'))
    print(search.common_first_name('female'))
    print(search.longest_timespan())
    print(search.month_most_new_releases())
    print(search.largest_increase())
    print(search.actresses_woody_harrelson())
    
