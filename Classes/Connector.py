import mysql.connector
from getpass import getpass
from mysql.connector import Error
from Classes.Person import *


def personcollection():
    global person_list
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="",
            database="comercio"

        )
        if mydb.is_connected():
            print('banco de dados conectado com sucesso')

            select_query = "SELECT C.ID_CLIENTE,C.NOME,C.SEXO,C.EMPREGO,IFNULL(C.EMAIL,'SEM EMAIL'),C.CPF,T.TIPO," \
                           "T.NUMERO " \
                           "FROM CLIENTE AS C " \
                           "INNER JOIN TELEFONE AS T ON ID_CLIENTE = IDCLIENTE; "

            cursor = mydb.cursor(buffered=True)

            cursor.execute(select_query)

            result = cursor.fetchall()
            print(result)

            person_list = []
            for i in result:
                print(i)
                person = Person(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                person_list.append(person)
            cursor.close()
        if mydb.is_connected():
            mydb.close()
        return person_list
    except Error as e:
        print("Error while connecting to MySQL", e)


class Connector():
    def __init__(self):
        pass
