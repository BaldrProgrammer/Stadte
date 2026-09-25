import psycopg2


conn = psycopg2.connect(
    database='stadte', user='admin', password='admin',
    host='localhost', port='5432'
)
cursor = conn.cursor()
cursor.execute('select * from stadte;')
alle = cursor.fetchall()
for stadt in alle:
    sql = f'''
    update stadte
    set ru_erste_buchstabe = '{stadt[1][0]}', ru_letzte_buchstabe = '{stadt[1][-1]}', en_erste_buchstabe = '{stadt[2][0]}', en_letzte_buchstabe = '{stadt[2][-1]}'
    where ru_name = '{stadt[1]}';
    '''
    print(sql)
    cursor.execute(sql)
    conn.commit()
