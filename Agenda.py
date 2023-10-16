import sqlite3
import os
from sqlite3 import Error

##CIRAR CONEXAO##
def ConexaoBanco():
    caminho="C:\\Users\\barbo\\OneDrive\\Área de Trabalho\\projeto bancodados\\agenda banco.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

def menuPrincipal():
    os.system("cls")
    print("1 - Novo Registro")
    print("2 - Deletar")
    print("3 - Atualizar")
    print("4 - Consultar")
    print("5 - Sair")

    opcao=0
    while opcao !=6:
        opcao=int(input("Digite a opcao: "))
        if opcao==1:
            inserir()
        elif opcao==2:
            deletar()
        elif opcao==3:
            atualizar()
        elif opcao==4:
            consultar()
        elif opcao==5:
            consultar()
        elif opcao==6:
            os.system("cls")
            print("Saindo")
            os.system("pause")
        else:
            os.system("cls")
            print("Opcao invalida")
            os.system("pause")




#criar tabala
#vsql="""CREATE TABLE tb_contatos_2 (
            #N_IDCONTATO       INTEGER   PRIMARY KEY AUTOINCREMENT,
            #T_NOMECONTATO     TEXT (30),
            #T_TELEFONECONTATO TEXT (15),
            #T_EMAILCONTATO    TEXT (30) 
        #);"""
def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as Ex:
        print(Ex)


#inserir
#nome=input("Digite o nome: ")
#telefone=input("Digite o telef: ")
#email=input("Digite o email: ")
#vsql="INSERT INTO tb_contatos_2  (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"' )"
def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com Sucesso!")
        #conexao.close

def inserir():
    os.system("cls")
    nome=input("Digite o nome: ")
    telefone=input("Digite o telef: ")
    email=input("Digite o email: ")
    vsql="INSERT INTO tb_contatos_2  (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"' )"  
    query(vcon, vsql)




#delatr
def deletar():   
    os.system("cls")
    idRemover=input('Digite o id para remoção: ')
    vsql="DELETE FROM tb_contatos_2  WHERE N_IDCONTATO="+idRemover+""
    query(vcon,vsql)


#atualizar
def atualizar():
    os.system("cls")
    vid=input('Digite o id para alterar: ')
    registro=consultar(vcon,"SELECT * FROM tb_contatos_2 WHERE N_IDCONTATO="+vid)
    rnome=registro[0][1]
    rtelefone=registro[0][2]
    remail=registro[0][3]
    NOVOnome=input("Digite o novo nome: ")
    NOVOtelefone=input("Digite o novo telef: ")
    NOVOemail=input("Digite o novo email: ")
    if(len(NOVOnome)==0):
        NOVOnome=rnome
    if(len(NOVOtelefone)==0):
        NOVOtelefone=rtelefone
    if(len(NOVOemail)==0):
        NOVOemail=remail
    vsql="UPDATE tb_contatos_2 SET T_NOMECONTATO='"+NOVOnome+"', T_TELEFONECONTATO='"+NOVOtelefone+"', T_EMAILCONTATO='"+NOVOemail+"' WHERE N_IDCONTATO="+vid
    query(vcon,vsql)




#consulta
def consultar():
    os.system("cls")
    print("Opções de consulta:")
    print("1 - Consultar por ID")
    print("2 - Consultar por Nome")
    opcao = int(input("Digite a opção de consulta: "))

    if opcao == 1:
        id_pesquisa = input("Digite o ID a ser pesquisado: ")
        sql = f"SELECT * FROM tb_contatos_2 WHERE N_IDCONTATO = {id_pesquisa}"
    elif opcao == 2:
        parte_nome = input("Digite parte do nome a ser pesquisada: ")
        sql = f"SELECT * FROM tb_contatos_2 WHERE T_NOMECONTATO LIKE '{parte_nome}%'"
    else:
        print("Opção inválida.")
        os.system("pause")
        return

    c = vcon.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    
    if resultado:
        for r in resultado:
            print(r)
    else:
        print("Nenhum resultado encontrado.")

    os.system("pause")


    

    
menuPrincipal()