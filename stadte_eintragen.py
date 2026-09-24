import psycopg2
from psycopg2.extras import execute_values


aus_website = '''
Аделаида	Adelaide	1 276 701	2014	Южная Австралия
Брисбен	Brisbane	2143121	2013	Квинсленд
Вуллонгонг	Wollongong	286581	2013	Новый Южный Уэльс
Серферс-Парадайс	Gold Coast	605134	2013	Квинсленд
Госфорд	Gosford	320266	2013	Новый Южный Уэльс
Дарвин	Darwin	119597	2013	Северная территория
Джелонг	Geelong	181853	2013	Виктория
Канберра	Canberra	418856	2013	Австралийская столичная территория
Кэрнс	Cairns	145003	2013	Квинсленд
Мельбурн	Melbourne	4181021	2013	Виктория
Ньюкасл	Newcastle	425895	2013	Новый Южный Уэльс
Перт	Perth	1901582	2013	Западная Австралия
Саншайн-Кост	Sunshine Coast	292354	2013	Квинсленд
Сидней	Sydney	4373433	2013	Новый Южный Уэльс
Таунсвилл	Townsville	176035	2013	Квинсленд
Тувумба	Toowoomba	112588	2013	Квинсленд
Хобарт	Hobart	206560	2013	Тасмания
'''


conn = psycopg2.connect(
    database='stadte', user='admin', password='admin',
    host='localhost', port='5432'
)
cursor = conn.cursor()
sql = f'''INSERT INTO stadte(ru_name, en_name, land_id) VALUES %s;'''

stadte_getrennt = aus_website.split('\n')
daten_zu_eintragen = []
for stadt in stadte_getrennt:
    stadt = stadt.split()
    daten_zu_eintragen.append((stadt[0], stadt[1], 1))

execute_values(cursor, sql, daten_zu_eintragen)
conn.commit()
cursor.close()
conn.close()
