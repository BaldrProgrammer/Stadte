import psycopg2
import random

conn = psycopg2.connect(
    database='stadte', user='admin', password='admin',
    host='localhost', port='5432'
)
cursor = conn.cursor()

lang = input('Wählen Sie bitte die Sprache des Spiels(ru/en): ')
benutzerbuchstabe = ''
stadte_waren = []

while True:
    benutzers_stadt = input('- ')
    stadte_waren.append(benutzers_stadt)
    sql = f'''select * from stadte where {lang}_erste_buchstabe = '{benutzers_stadt[-1].upper()}';'''
    cursor.execute(sql)
    passende_antworten = cursor.fetchall()

    while True:
        antwort = random.choice(passende_antworten)
        if antwort[1] in stadte_waren:
            continue
        break

    print('~', antwort[1])
    stadte_waren.append(antwort[1])
