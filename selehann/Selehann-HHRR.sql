-- create database hr;

CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `fisrtname` varchar(255),
  `lastname` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `skills` (
  `id` integer PRIMARY KEY,
  `skill_name` varchar(255)
);

CREATE TABLE `user_skills` (
  `skill_id` int,
  `user_id` int
);

ALTER TABLE `user_skills` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
ALTER TABLE `user_skills` ADD FOREIGN KEY (`skill_id`) REFERENCES `skills` (`id`);
alter table skills add column rating int;

select * from users;
select * from skills;
select * from user_skills;

select u.id, u.fisrtname, us.skill_id from users u
join user_skills us on us.user_id = u.id
where skill_id in (select id from skills where rating <= 10)
order by u.id, us.skill_id;

select id from skills where rating <= 10;

select id from (
select u.id, count(skill_id) total_top_skill from users u
join user_skills us on us.user_id = u.id
where skill_id in (select id from skills where rating <= 10)
group by u.id) as t1
where total_top_skill >= 5;
