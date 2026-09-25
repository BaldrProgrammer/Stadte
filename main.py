import psycopg2

conn = psycopg2.connect(
    database='stadte', user='admin', password='admin',
    host='localhost', port='5432'
)
cursor = conn.cursor()

lang = input('Wählen Sie bitte die Sprache des Spiels(ru/en): ')
stadte_waren = []

while True:
    benutzers_stadt = input('- ')
    sql = f'select * from stadte where {lang}_erste_buchstabe = {benutzers_stadt[-1].upper()};'
    print(sql)
