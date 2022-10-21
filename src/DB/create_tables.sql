CREATE DATABASE poketrackerdb;
use poketrackerdb;

CREATE TABLE Trainer(
    name VARCHAR(255) PRIMARY KEY,
    town VARCHAR(255)
);

CREATE TABLE Pokemon(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    height INT,
    weight INT
);

CREATE TABLE Type(
    pokeType VARCHAR(255) PRIMARY KEY
);

CREATE TABLE PokemonTrainer(
    pokemonId INT,
    trainerName VARCHAR(255),
    PRIMARY KEY(pokemonId, trainerName),
    FOREIGN KEY(pokemonId) REFERENCES Pokemon(id),
    FOREIGN KEY(trainerName) REFERENCES Trainer(name)
);

CREATE TABLE PokemonType(
    pokemonId INT,
    pokeType VARCHAR(255),
    PRIMARY KEY(pokemonId, pokeType),
    FOREIGN KEY(pokemonId) REFERENCES Pokemon(id),
    FOREIGN KEY(pokeType) REFERENCES Type(pokeType)  
);


