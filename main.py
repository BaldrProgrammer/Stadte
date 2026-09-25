import psycopg2
import random

conn = psycopg2.connect(
    database='stadte', user='admin', password='admin',
    host='localhost', port='5432'
)
cursor = conn.cursor()

lang = input('Wählen Sie bitte die Sprache des Spiels(ru/en): ')
benutzerbuchstabe = None
stadte_waren = []

while True:
    benutzers_stadt = input('- ')
    if benutzers_stadt in stadte_waren:
        print('!! Diese Stadt war schon')
        continue
    # print(benutzers_stadt.lower()[0], benutzerbuchstabe)
    if benutzers_stadt.lower()[0] != benutzerbuchstabe and benutzerbuchstabe:
        print(f'!! Falscher Anfangsbuchstabe. Sie haben an {benutzerbuchstabe}')
        continue

    stadte_waren.append(benutzers_stadt.lower())
    nachste_buchstabe = benutzers_stadt[-1].upper()
    match nachste_buchstabe:
        case 'Ь':
            nachste_buchstabe = benutzers_stadt[-2].upper()
        case 'Ы':
            nachste_buchstabe = 'И'
        case 'Е':
            nachste_buchstabe = 'Э'

    sql = f'''select * from stadte where {lang}_erste_buchstabe = '{nachste_buchstabe}';'''
    cursor.execute(sql)
    passende_antworten = cursor.fetchall()

    while True:
        antwort = random.choice(passende_antworten)
        if antwort[1] in stadte_waren:
            continue
        break

    print('~', antwort[1], '\n')
    stadte_waren.append(antwort[1].lower())
    benutzerbuchstabe = antwort[1][-1].lower()
    match benutzerbuchstabe:
        case 'ь':
            benutzerbuchstabe = antwort[1][-2].lower()
        case 'ы':
            benutzerbuchstabe = 'и'
