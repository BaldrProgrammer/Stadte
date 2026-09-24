import psycopg2
from psycopg2.extras import execute_values

from translate import Translator
translator = Translator(from_lang='russian', to_lang='english')


aus_website = '''
Вена (нем. Wien)	1766746	2014	Вена
Грац (нем. Graz)	269997	2014	Штирия
Зальцбург (нем. Salzburg)	146631	2014	Зальцбург
Инсбрук (нем. Innsbruck)	124579	2014	Тироль
Линц (нем. Linz)	193814	2014	Верхняя Австрия
'''


conn = psycopg2.connect(
    database='stadte', user='admin', password='admin',
    host='localhost', port='5432'
)
cursor = conn.cursor()
sql = f'''INSERT INTO stadte(ru_name, en_name, land_id) VALUES %s;'''

stadte_getrennt = aus_website.split('\n')
print(stadte_getrennt)
daten_zu_eintragen = []

for stadt in stadte_getrennt:
    try:
        stadt = stadt.split()
        en_name = translator.translate(stadt[0])
        daten_zu_eintragen.append((stadt[0], en_name, 1))
    except IndexError:
        print('index Fehlung, stadt - ', stadt)

print(daten_zu_eintragen)
execute_values(cursor, sql, daten_zu_eintragen)
conn.commit()
cursor.close()
conn.close()
