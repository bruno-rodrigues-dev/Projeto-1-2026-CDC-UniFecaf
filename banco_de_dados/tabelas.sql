CREATE DATABASE IF NOT EXISTS projeto_unifecaf;
USE projeto_unifecaf;

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL
);

CREATE TABLE marcas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_marca VARCHAR(50) NOT NULL
);

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    valor DECIMAL(10, 2) NOT NULL,
    categoria_id INT,
    marca_id INT,

    CONSTRAINT fk_categoria
    FOREIGN KEY (categoria_id)
    REFERENCES categorias(id)
    ON DELETE CASCADE,

    CONSTRAINT fk_marca
    FOREIGN KEY (marca_id)
    REFERENCES marcas(id)
    ON DELETE CASCADE
);