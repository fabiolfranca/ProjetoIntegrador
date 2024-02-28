import os
import mysql.connector 
from mysql.connector import Error
import time

def criarBD(host, usuario, senha, DB):
    try:
        connection=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'admin',
            database = 'empresa'
        )
        print("Banco de dados já existe!")
        return True
    except Error as err:
        print("Banco de dados não existe, criando banco de dados...")
        pass
    connection=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'admin',
        )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE "+ DB)
    cursor.close()
    connection.close()
    print("Banco de dados criado com sucesso!")
    return False


def criarTabela(host, usuario, senha, DB):
    connection=conectarBD (host, usuario, senha, DB)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Funcionario (idFuncionario int auto_increment primary key, Nome varchar(45), Email varchar(45), Telefone varchar(15), Rua varchar(45), Bairro varchar(45), DataAdmissao date)")
    cursor.execute("CREATE TABLE Licenca (idLicenca int auto_increment primary key, Licenca varchar(45), ValorFinal float, Validade varchar(9)")
    cursor.execute("CREATE TABLE Software (idSoftware int auto_increment primary key, Software varchar(30), idLicenca int, foreign key (idLicenca) references Licenca(idLicenca)")
    cursor.execute("CREATE TABLE Equipamento (idEquipamento int auto_increment primary key, Equipamento varchar(45), QtdEquipamento int, idSoftware int, foreign key (idSoftware) references Software(idSoftware)")
    cursor.execute("CREATE TABLE Setor (idSetor int auto_increment primary key, NomeSetor varchar(45), QtdFuncionarios int, idFuncionario int, idEquipamento int, foreign key (idFuncionario) reference Funcionario(idFuncionario), foreign key (idEquipamento) references Equipamento(idEquipamento)")
    cursor.close()
    connection.close()
    print("Tabela criada com sucesso!")


def conectarBD (host, usuario, senha, DB):
    try:
        connection=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'admin',
            database = 'empresa'
        )
        print("Conexão estabelecida com sucesso!")
        return connection
    except Error as err:
        print("Erro ao estabelecer conexão com o banco de dados: ",err)
        exit()

def insertBD(nome, rg, cpf, endereco,cidade,uf,conn):
    connection = conn
    cursor = connection.cursor()

    sql = "INSERT INTO FUNCIONARIO (Nome, Email, Telefone, Rua, Bairro, DataAdmissao) VALUES(%s,%s,%s,%s,%s,%s)"
    data = (
        'Lucas Aguilera Martins',
        'lucasmartinsaguilera@gmail.com ',
        '(15) 99877-6655',
        'Coronel Nogueira Padilha',
        'Vila Hortência',
        '2023-09-09'
    )
    cursor.execute(sql,data)
    connection.commit()

    funcionario_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Foi cadastrado o novo funcionario de ID ",funcionario_id)


def read_BD(conn):
    connection = conn
    cursor = connection.cursor() 

    sql = "SELECT * FROM funcionario"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    for result in results:
        print(result)


def updateBD(Nome, Telefone, Rua, Bairro, id, conn):
    connection = conn
    cursor = connection.cursor()
    sql = "UPDATE FUNCIONARIO SET NOME=%s, TELEFONE=%s, RUA=%s, BAIRRO=%s WHERE ID=%s"
    data = (
        'Lucas Aguilera Martins',
        '(15) 99877-6655',
        'Coronel Nogueira Padilha',
        'Vila Hortência',
        '1'
    )
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros atualizados")


def deleteBD(id, conn):
    connection = conn 
    cursor = connection.cursor()
    sql = "DELETE FROM FUNCIONARIO WHERE ID = %s"
    data = ('1')
    cursor.execute(sql,data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " registros removidos")


def main():
    if not criarBD("localhost","root", "root", "projeto"):
        criarTabela("localhost","root", "root", "projeto")
    time.sleep(3)
    while(True):
        os.system("cls")
        def main():
            while True:
                print("\n\n:::::: GERENCIADOR DE CADASTRO DE funcionarioS ::::::")
                print("1 - Cadastrar funcionario")
                print("2 - Exibir funcionarios cadastrados")
                print("3 - Atualizar dados do funcionario")
                print("4 - Deletar cadastro do funcionario")
                print("5 - Sair")

        opcao = input("Digite a opção desejada:")
        

        if opcao == "1":
            nome = input("Digite o nome completo do funcionario:")
            verificar_nome(nome)
            email = input("Digite o email:")
            verificar_email(email)
            telefone = input("Digite o Telefone:")
            verificar_telefone(telefone)
            rua = input("Digite o endereço:")
            bairro = input("Digite o bairro:")
            verificar_endereco(rua, bairro)
            dataadmissao= input("Digite a data de admissão:")
            verificar_data(dataadmissao)

            connection = conectarBD("localhost","root", "admin", "empresa")
            insertBD(nome, rua, telefone, rua, bairro, dataadmissao, connection)
            time.sleep(5)
        elif opcao == "2":
            connection = conectarBD("localhost","root", "admin", "empresa")
            read_BD(connection)
            time.sleep(5)
        
        elif opcao == "3":
            connection = conectarBD("localhost","root", "admin", "empresa")
            id = input("Informe o ID do funcionario: ")
            nome = input("Informe o nome atualizado: ")
            verificar_nome(nome)
            rua = input("Informe o nome da rua: ")
            bairro = input("Informe o bairro atual: ")
            verificar_endereco(rua, bairro)
            telefone = input("Informe o telefone: ")
            verificar_telefone(telefone)
            updateBD(nome, rua, bairro, telefone, id, connection)
            time.sleep(5)
        elif opcao == "4":
            connection = conectarBD("localhost","root", "admin", "empresa")
            id = input("Informe o ID do Funcionario:")
            deleteBD(id, connection)
            time.sleep(5)
        elif opcao == "5":
            break

if __name__ == "__main__":
    main()

    def verificar_email(email): 
        if '@' in email:
            print("Email válido.")
else:
    print("Email inválido. Por favor, insira um email que contenha '@'.")

def verificar_nome(nome):
    if nome.isalpha():
        print("Nome válido.")
    else:
        print("Nome inválido. Por favor, insira um nome que contenha apenas letras.")

def verificar_telefone(telefone):
    if telefone.isdigit():
        print("Telefone válido.")
    else:
        print("Telefone inválido. Por favor, insira um número de telefone que contenha apenas números.")

def verificar_endereco(rua, bairro):
    if rua and bairro:
        print("Endereço válido.")
    else:
        print("Endereço inválido. Por favor, insira um endereço completo.")

def verificar_data(dataadmissao):
    if dataadmissao:
        print("Data de admissão válida.")
    else:
        print("Data de admissão inválida. Por favor, insira uma data de admissão.")
