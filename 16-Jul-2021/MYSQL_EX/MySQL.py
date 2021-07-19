import mysql.connector

con = mysql.connector.connect(user = 'root', password = 'mysql',host='localhost')

print(con)

cur  =con.cursor()

cur.execute("CREATE DATABASE studentdb")

cur.execute("SHOW DATABASES")

for database in cur:
    print(database)