CREATE DATABASE centre_formation;
USE centre_formation;

CREATE TABLE apprenants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    promo VARCHAR(10) NOT NULL,
    presence ENUM('Absent','Présent') DEFAULT 'Absent'
);
