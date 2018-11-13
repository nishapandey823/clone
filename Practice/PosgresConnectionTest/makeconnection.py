import psycopg2
conn = psycopg2.connect(database='', user='postgres', password='postgres', host='localhost', port="5432")
cursor = conn.cursor()
cursor.execute('SELECT count(*) as count FROM employee')
cursor.execute('SELECT * FROM employee')

row = cursor.fetchone()

conn.close()

print(row)