-- Check missing data

-- shows with missig actor
SELECT show_id FROM actor_bridge WHERE actor_id = (
  SELECT id FROM actor_dim WHERE name = ''
);

-- shows with missig type
SELECT id FROM shows WHERE type_id = (
  SELECT id FROM type_dim WHERE type = ''
);

-- shows with missig director
SELECT show_id FROM director_bridge WHERE director_id = (
  SELECT id FROM director_dim WHERE name = ''
);

-- shows with missig country
SELECT show_id FROM country_bridge WHERE country_id = (
  SELECT id FROM country_dim WHERE country = ''
);

-- shows with missig rating
SELECT id FROM shows WHERE rating_id = (
  SELECT id FROM rating_dim WHERE rating = ''
);

-- shows with missig duration
SELECT id FROM shows WHERE duration_id = (
  SELECT id FROM duration_dim WHERE duration = ''
);

-- shows with missig category
SELECT show_id FROM category_bridge WHERE category_id = (
  SELECT id FROM category_dim WHERE category = ''
);

-- Non valida data
SELECT id FROM shows WHERE date_added IS NULL;
SELECT id FROM shows WHERE release_year IS NULL;


