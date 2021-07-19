import mysql.connector

con = mysql.connector.connect(
    user='user',
    password='pass',
    host='1.2.3.4',
    database='test'
)

word = input("give me a word: ")

cursor = con.cursor()
# noinspection SqlNoDataSourceInspection
query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = \'{word}\'")
results = cursor.fetchall()

if len(results) == 0:
    print('no results found')
    exit(1)

print('found', len(results), 'results')
c = 1
for res in results:
    print(c, "-", res[0])
    c += 1