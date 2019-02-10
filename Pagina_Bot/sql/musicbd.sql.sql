CREATE DATABASE music18;

USE music18;

CREATE TABLE instrumentos(
    nombre varchar(50) NOT NULL PRIMARY KEY,
    marca varchar(50) NOT NULL,
    modelo varchar(50) NOT NULL,
    color varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO instrumentos (nombre, marca, modelo, color) VALUES 
('Guitarra', 'Yamaja', 'electrica', 'roja'),
('Bajo', 'guipson', 'electrico', 'verde'),
('teclado', 'bj', 'clasico', 'negro'),
('Violin', 'iho', 'clasico', 'cafe'),
('Bateria', 'yamaja', 'clasica', 'roja');

SHOW TABLES;

DESCRIBE instrumentos;

SELECT * FROM instrumentos;

CREATE USER 'music'@'localhost' IDENTIFIED BY 'music.2019';
GRANT ALL PRIVILEGES ON music18.* TO 'music'@'localhost';
FLUSH PRIVILEGES;
