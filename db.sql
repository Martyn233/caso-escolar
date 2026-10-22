create database caso_escolar; 

CREATE USER 'Martyn'@'%' IDENTIFIED BY '123456789';
CREATE USER 'Martyn'@'localhost' IDENTIFIED BY '123456789';

GRANT ALL PRIVILEGES ON caso_escolar.* TO 'Martyn'@'%';
GRANT ALL PRIVILEGES ON caso_escolar.* TO 'Martyn'@'localhost';

FLUSH PRIVILEGES;