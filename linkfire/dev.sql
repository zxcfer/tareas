show tables;
select * from shows;
select * from type_dim;
select * from director_bridge;
select * from director_dim;
select * from actor_bridge;
select * from actor_dim;
select * from country_bridge;
select * from country_dim;
select * from rating_dim;
select * from duration_dim;
select * from category_bridge;
select * from category_dim;

select * from shows where id = 12;
select * from director_bridge where show_id = 13;
select * from director_dim where id = 12;
select * from category_bridge where show_id = 13;

