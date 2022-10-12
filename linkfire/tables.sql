CREATE DATABASE shows;

DROP TABLE IF EXISTS shows;
CREATE TABLE shows (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    type_id BIGINT UNSIGNED NOT NULL,
    date_added DATE DEFAULT NULL,
    release_year INT UNSIGNED NOT NULL,
    rating_id BIGINT UNSIGNED NOT NULL,
    duration_id BIGINT UNSIGNED NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS type_dim;
CREATE TABLE type_dim (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    type VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS director_bridge;
CREATE TABLE director_bridge (
    show_id BIGINT UNSIGNED NOT NULL,
    director_id BIGINT UNSIGNED NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS director_dim;
CREATE TABLE director_dim (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) UNIQUE NOT NULL,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS actor_bridge;
CREATE TABLE actor_bridge (
    show_id BIGINT UNSIGNED NOT NULL,
    actor_id BIGINT UNSIGNED NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS actor_dim;
CREATE TABLE actor_dim (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) UNIQUE NOT NULL,
    gender INT DEFAULT 0,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS country_bridge;
CREATE TABLE country_bridge (
    show_id BIGINT UNSIGNED NOT NULL,
    country_id BIGINT UNSIGNED NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS country_dim;
CREATE TABLE country_dim (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    country VARCHAR(200) UNIQUE NOT NULL,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS rating_dim;
CREATE TABLE rating_dim (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    rating VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS duration_dim;
CREATE TABLE duration_dim (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    duration VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS category_bridge;
CREATE TABLE category_bridge (
    show_id BIGINT UNSIGNED NOT NULL,
    category_id BIGINT UNSIGNED NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DROP TABLE IF EXISTS category_dim;
CREATE TABLE category_dim (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY (id)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
