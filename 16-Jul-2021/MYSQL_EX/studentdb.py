import mysql.connector
from mysql.connector import cursor

con = mysql.connector.connect(user = 'root', password = 'mysql',host='localhost',database = "studentdb")

print(con)

cur  =con.cursor()
cur.execute("CREATE TABLE studentinfo(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), subject VARCHAR(255))")

query = "INSERT INTO studentinfo(name,subject) VALUES (%s,%s)"
value = ("Ram", "Science")
cur.execute(query,value)
print("Row Inserted")

values = [("Raja","Social"),("Ratha","Maths"),("Krish","Computer")]
cur.executemany(query,values)
print("Many Rows Insserted")

print("All rows in the table")
cur.execute("SELECT * FROM studentinfo")
all_details=cur.fetchall()
for n in all_details:
    print(n)

print("Details of krish")
cur.execute("SELECT * FROM studentinfo where name ='Krish'")
print(cur.fetchall())