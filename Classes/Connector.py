import mysql.connector
from getpass import getpass
from mysql.connector import Error
from Classes.Person import *


def check_cpf(cpf):
    valida = False
    lista_firstDigit = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    cpf_inserido = cpf.replace(".", "")
    cpf_inserido = cpf_inserido.replace("-", "")
    cpf_inserido = list(cpf_inserido)
    cpf_teste = cpf_inserido.copy()
    cpf_teste.pop(-1)
    cpf_teste.pop(-1)
    cpf_testeConvertido = []
    for l in cpf_teste:
        cpf_testeConvertido.append(int(l))

    lista_firstD = []
    a = 0
    b = 0
    for i in cpf_testeConvertido:
        int(i)

        a = i * lista_firstDigit[b]
        lista_firstD.append(a)
        b += 1

    resultado = 0
    for l in lista_firstD:
        resultado += l

    primeiro_digito = (11 - (resultado % 11))
    if primeiro_digito > 9:
        cpf_testeConvertido.append(0)
    else:
        cpf_testeConvertido.append(primeiro_digito)

    list_SecondDigit = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    m = 0
    n = 0
    list_secondD = []
    for j in cpf_testeConvertido:
        m = j * list_SecondDigit[n]
        list_secondD.append(m)
        n += 1

    second_result = 0
    for p in list_secondD:
        second_result += p

    segundo_digito = (11 - (second_result % 11))

    if segundo_digito > 9:
        cpf_testeConvertido.append(0)
    else:
        cpf_testeConvertido.append(segundo_digito)
    cpf_inserido_convertido = []
    for i in cpf_inserido:
        cpf_inserido_convertido.append(int(i))

    if set(cpf_testeConvertido) == set(cpf_inserido_convertido):
        print('CPF Válido')
        valida = True
        return valida

    else:
        print('CPF invalido')
        valida = False
        return valida


def search_cpf(cpf):
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
            select_query = "SELECT C.ID_CLIENTE,C.NOME,C.SEXO,C.EMPREGO,IFNULL(C.EMAIL,'SEM EMAIL'),C.CPF,T.TIPO,T.NUMERO " \
                           "FROM CLIENTE AS C " \
                           "INNER JOIN TELEFONE AS T " \
                           "ON ID_CLIENTE = IDCLIENTE " \
                           "WHERE C.CPF=%s;"
            values = (cpf,)
            cursor = mydb.cursor(buffered=True)
            cursor.execute(select_query, values)
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
            values = (Person.name, Person.sex, Person.job, Person.email, Person.cpf, Person.id)
            update_telquery = "UPDATE TELEFONE SET TIPO = %s, Numero = %s WHERE (IDCLIENTE = %s); "
            phone_values = (Person.typephone, Person.phone_number, Person.id)
            cursor.execute(update_cliquery, values)
            cursor.execute(update_telquery, phone_values)
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
            cursor.execute(delete_phonequery, values)
            cursor.execute(delete_query, values)
            mydb.commit()

    except Error as e:
        print(e)
