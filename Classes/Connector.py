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

            person_list = []
            for i in result:
                person = Person(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                person_list.append(person)
            cursor.close()
        if mydb.is_connected():
            mydb.close()
        return person_list
    except Error as e:
        print("Error while connecting to MySQL", e)


def insert_person(Person):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="",
            database="comercio"

        )
        if mydb.is_connected():
            insert_cliquery = "INSERT INTO CLIENTE(NOME,SEXO,EMPREGO,EMAIL,CPF) VALUES(%s,%s,%s,%s,%s);"
            insert_phonequery = "INSERT INTO TELEFONE(TIPO,NUMERO,IDCLIENTE) VALUES(%s,%s,%s);"
            cursor = mydb.cursor()
            values = (Person.name, Person.sex, Person.job, Person.email, Person.cpf)
            cursor.execute(insert_cliquery, values)
            values_phone = (Person.typephone, Person.phone_number, cursor.lastrowid)
            cursor.execute(insert_phonequery, values_phone)
            userid = cursor.lastrowid
            mydb.commit()
            cursor.close()
            mydb.close()
            print('foi cadastrado o novo usuario de ID:', userid)

    except Error as e:
        print(f'Erro in insert{e}')


def update_person(Person):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="",
            database="comercio"

        )
        if mydb.is_connected():
            cursor = mydb.cursor()
            update_cliquery = "UPDATE CLIENTE SET NOME= %s,SEXO = %s, EMPREGO = %s, EMAIL = %s, CPF = %s WHERE " \
                           "(ID_CLIENTE = %s); "
            values = (Person.name,Person.sex,Person.job,Person.email,Person.cpf,Person.id)
            update_telquery = "UPDATE TELEFONE SET TIPO = %s, Numero = %s WHERE (IDCLIENTE = %s); "
            phone_values = (Person.typephone, Person.phone_number, Person.id)
            cursor.execute(update_cliquery,values)
            cursor.execute(update_telquery,phone_values)
            mydb.commit()
            cursor.close()
            mydb.close()
            print('deu bom garai')
    except Error as e:
        print(e)

def delete_person(id):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="",
            database="comercio"

        )
        if mydb.is_connected():
            cursor = mydb.cursor()
            delete_phonequery = "DELETE FROM TELEFONE WHERE (IDCLIENTE = %s);"
            delete_query = "DELETE FROM CLIENTE WHERE (ID_CLIENTE = %s);"
            values = (id,)
            cursor.execute(delete_phonequery,values)
            cursor.execute(delete_query,values)
            mydb.commit()

    except Error as e:
        print(e)


