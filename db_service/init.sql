-- Création de la table my_table si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS feedback (
    -- Commentaire et note
    id SERIAL PRIMARY KEY,
    comment TEXT,
    rating INT
);

insert into feedback (comment, rating) values ('Test de commentaire', 1);