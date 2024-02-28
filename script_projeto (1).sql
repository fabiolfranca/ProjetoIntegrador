CREATE DATABASE EMPRESA;
USE EMPRESA;

CREATE TABLE Funcionarios (
	idFuncionario INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(45),
    Email VARCHAR(45),
    Telefone VARCHAR(45),
    Rua VARCHAR(45),
    Bairro VARCHAR(45),
    DataAdmissao DATE
);

CREATE TABLE Setor (
	idSetor INT PRIMARY KEY AUTO_INCREMENT,
    NomeSetor VARCHAR(45),
    DescricaoSetor VARCHAR(500),
    QtdFuncionarios INT,
    idEquipamento INT,
    idFuncionario INT,
    FOREIGN KEY (idEquipamento) REFERENCES Equipamentos(idEquipamento),
    FOREIGN KEY (idFuncionario) REFERENCES Funcionarios(idFuncionario)
);

CREATE TABLE Equipamentos (
	idEquipamento INT PRIMARY KEY AUTO_INCREMENT,
    Equipamento VARCHAR(25),
    QtdEquipamentos INT,
    idSoftware INT,
    FOREIGN KEY (idSoftware) REFERENCES Softwares(idSoftware)
);

CREATE TABLE Softwares (
	idSoftware INT PRIMARY KEY AUTO_INCREMENT,
    Software VARCHAR(40),
    idLicenca INT,
    FOREIGN KEY (idLicenca) REFERENCES Licencas(idLicenca)
);

CREATE TABLE Licencas (
	idLicenca INT PRIMARY KEY AUTO_INCREMENT,
    Licenca VARCHAR(40),
    ValorFinal FLOAT,
    Validade VARCHAR(10)
);

SELECT * FROM FUNCIONARIOS;