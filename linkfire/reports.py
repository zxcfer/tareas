from base import Base


class Validator(Base):

    def shows_missing_actors(self):
        sql = """
        SELECT show_id FROM actor_bridge WHERE actor_id = (
            SELECT id FROM actor_dim WHERE name = '');
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def shows_missing_type(self):
        sql = """
        SELECT id FROM shows WHERE type_id = (
          SELECT id FROM type_dim WHERE type = ''
        );
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def shows_missing_director(self):
        sql = """
        SELECT show_id FROM director_bridge WHERE director_id = (
          SELECT id FROM director_dim WHERE name = ''
        );
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def shows_missing_country(self):
        sql = """
        SELECT show_id FROM country_bridge WHERE country_id = (
          SELECT id FROM country_dim WHERE country = ''
        );
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def shows_missing_rating(self):
        sql = """
        SELECT id FROM shows WHERE rating_id = (
          SELECT id FROM rating_dim WHERE rating = ''
        );
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def shows_missing_duration(self):
        sql = """
        SELECT id FROM shows WHERE duration_id = (
          SELECT id FROM duration_dim WHERE duration = ''
        );
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def shows_missing_category(self):
        sql = """
        SELECT show_id FROM category_bridge WHERE category_id = (
          SELECT id FROM category_dim WHERE category = ''
        );
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    

if __name__ == '__main__':
    validator = Validator()
    print('Shows missing actors')
    print(validator.shows_missing_actors())
    print('Shows missing type')
    print(validator.shows_missing_type())
    print('Shows missing director')
    print(validator.shows_missing_director())
    print('Shows missing country')
    print(validator.shows_missing_country())
    print('Shows missing rating')
    print(validator.shows_missing_rating())
    print('Shows missing duration')
    print(validator.shows_missing_duration())
    print('Shows missing category')
    print(validator.shows_missing_category())
