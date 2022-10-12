-- What is the most common first name among actors and actresses?
SELECT first_name, count(*) as total FROM (
SELECT 
    id,
    if( INSTR(`name`, ' ')=0, 
      TRIM(SUBSTRING(`name`, INSTR(`name`, ' ')+1)), 
      TRIM(SUBSTRING(`name`, 1, INSTR(`name`, ' ')-1)) ) AS first_name,
    gender
FROM actor_dim
WHERE gender = 1) as T
GROUP BY first_name
ORDER BY total DESC
LIMIT 1;

SELECT first_name, count(*) as total FROM (
SELECT 
    id, 
    if( INSTR(`name`, ' ')=0, 
      TRIM(SUBSTRING(`name`, INSTR(`name`, ' ')+1)), 
      TRIM(SUBSTRING(`name`, 1, INSTR(`name`, ' ')-1)) ) AS first_name,
    gender
FROM actor_dim
WHERE gender = 2) as T
GROUP BY first_name
ORDER BY total desc
LIMIT 1;

-- Which Movie had the longest timespan from release to appearing on Netflix?
SELECT id, title, date_added, release_year, 
  DATEDIFF(date_added, CONCAT_WS('-', release_year, 01, 01)) AS timespan
FROM shows ORDER BY timespan DESC LIMIT 1;

-- Which Month of the year had the most new releases historically?
SELECT month_added, count(id) as total FROM (
    SELECT id, MONTH(date_added) month_added FROM shows) AS T
GROUP BY month_added
ORDER BY total DESC
LIMIT 1;

-- Which year had the largest increase year on year (percentage wise) for TV Shows?
set @prev=0;
SELECT year_added, curr_total-lag_total as delta FROM (
SELECT year_added, @prev lag_total, @prev:=total curr_total FROM (
SELECT year_added, count(id) as total FROM (
    SELECT id, YEAR(date_added) year_added FROM shows 
    WHERE date_added is not null AND type_id = 1) AS T
GROUP BY year_added
ORDER BY year_added) as T2) as T3 ORDER BY delta DESC LIMIT 1;

-- List the actresses that have appeared in a movie with Woody Harrelson more than once.
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
);
