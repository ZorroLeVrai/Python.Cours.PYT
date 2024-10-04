--Création de la table d'utilisateurs
CREATE TABLE utilisateurs (
    id INT GENERATED ALWAYS AS IDENTITY,  -- Identifiant unique pour chaque utilisateur, auto-incrémenté
    nom VARCHAR(100) NOT NULL,  -- Nom de l'utilisateur
    email VARCHAR(150) UNIQUE NOT NULL,  -- Adresse email unique et obligatoire
    mot_de_passe VARCHAR(50) NOT NULL,  -- Mot de passe de l'utilisateur
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Date d'inscription avec une valeur par défaut
);

--Insertion des données dans la table d'utilisateurs
INSERT INTO utilisateurs (nom, email, mot_de_passe) VALUES
('Alice Dupont', 'alice.dupont@example.com', 'password1'),
('Bob Martin', 'bob.martin@example.com', 'password2'),
('Charlie Durand', 'charlie.durand@example.com', 'password3'),
('Diane Leroy', 'diane.leroy@example.com', 'password4');
