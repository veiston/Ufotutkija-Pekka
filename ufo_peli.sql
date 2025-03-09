DROP DATABASE IF EXISTS ufo_peli;
CREATE DATABASE ufo_peli;
USE ufo_peli;

CREATE TABLE airport(
ident VARCHAR(40) NOT NULL,
name VARCHAR(40) NOT NULL,
municipality VARCHAR(40),
player_location VARCHAR(40) NOT NULL,
PRIMARY KEY (ident)
);

CREATE TABLE items(
name VARCHAR(40) NOT NULL,
price INT,
item_type VARCHAR(40),
description VARCHAR(2000),
is_finite BIT,
PRIMARY KEY (name)
);

CREATE TABLE player(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(40) DEFAULT 'Pekka',
location_ident VARCHAR(40) DEFAULT 'EFHK',
hp INT DEFAULT 200,
money INT DEFAULT 0,
player_level INT DEFAULT 1,
PRIMARY KEY (id),
FOREIGN KEY (location_ident) REFERENCES airport(ident)
);

CREATE TABLE inventory(
player_id INT,
item VARCHAR(40),
amount INT,
PRIMARY KEY (player_id, item),
FOREIGN KEY (player_id) REFERENCES player(id),
FOREIGN KEY (item) REFERENCES items(name)
);

CREATE TABLE creature_types(
name VARCHAR(40) NOT NULL,
hp INT,
attack INT,
weakness VARCHAR(40),
PRIMARY KEY (name)
);

CREATE TABLE creature(
name VARCHAR(40) NOT NULL,
creature_type VARCHAR(40),
description VARCHAR(2000),
location_ident VARCHAR(40),
PRIMARY KEY (name),
FOREIGN KEY (creature_type) REFERENCES creature_types(name),
FOREIGN KEY (location_ident) REFERENCES airport(ident)
);

INSERT INTO airport(ident, name, municipality, player_location)
VALUES ('EFHK', 'Helsinki-Vantaan lentoasema', 'Vantaa', 'Helsinki'),
('KBNA', 'Nashville International Airport', 'Nashville', 'Evergreen'),
('KDEN', 'Denver International Airport', 'Denver', 'Hopkinsville'),
('KHTS', 'Tri-State/Milton J. Ferguson Field', 'Huntington', 'Flatwoods'),
('KLFK', 'Angelina County Airport', 'Lufkin', 'Broaddus'),
('KROW', 'Roswell Air Center Airport', 'Roswell', 'Roswell'),
('KSEA', 'Seattle Tacoma International Airport', 'Seattle', 'Aberdeen');

INSERT INTO items(name, price, item_type, description, is_finite)
VALUES ('Nokia', NULL, 'Phone', 'Your trusty phone. Indestructible.', 0),
('Water Balloon', 50, 'Water', 'Balloon that contains water.', 1),
('Salt', 50, 'Salt', 'Handful of salt.', 1);

INSERT INTO creature_types(name, hp, attack, weakness)
VALUES ('Alien', 100, 20, 'Water'),
('Ghost', 70, 30, 'Salt'),
('Melvin', 200, 40, 'Phone');

INSERT INTO creature(name, creature_type, description, location_ident)
VALUES ('Metal Goblin', 'Alien', 'Horrible small creature that apparently burns with the desire to bite your ankles and to steal your phone.', 'KBNA'),
('Braxie', 'Alien', 'Huge floating creature of weird shapes. Smells really bad.', 'KBNA'),
('Wounded Grey', 'Alien', 'Disoriented lanky creature. Very aggressive.', 'KROW'),
('Texaboo Baba Yaga', 'Ghost', 'Old lady wearing a Texas costume riding a KFC bucket. Threatening you with guns.', 'KLFK'),
('Näkki', 'Ghost', 'Very wet creature.', 'KSEA'),
('Mutated Melvin', 'Melvin', 'Your old friend seems off.', 'KBNA');
