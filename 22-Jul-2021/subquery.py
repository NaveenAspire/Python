import mysql.connector


con = mysql.connector.connect(user = "root",
password="mysql",host="localhost",database="employee")

print(con)

cur = con.cursor()
try:
    cur.execute("""create table emp(id int auto_increment primary key, name varchar(20), age int, 
    doj date, dept varchar(10), city varchar(20),
    salary int)""")

    cur.execute("ALTER TABLE emp auto_increment=101")
except:
    print("table exist")


insert = """INSERT INTO emp(name,age,doj,dept,city,salary) values(%s,%s,%s,%s,%s,%s)"""

values = [("abi",23,'2020-05-13',"CSE","mumbai",20000),("anbu",24,'2020-05-02',"IT","chennai",25000),
("varun",23,'2020-06-13',"ECE","bangalore",23000),("tharun",25,'2019-05-13',"CSE","delhi",20000),
("mahesh",23,'2020-05-17',"Finance","singapore",30000),("ramesh",23,'2020-05-02',"EEE","Salem",24000)]

cur.executemany(insert,values)
con.commit()

cur.execute("SELECT name FROM emp WHERE salary=(select MAX(salary) from emp)")

high_salary = cur.fetchone()
print("Highest Salary : "+high_salary[0])

cur.execute("SELECT name,salary FROM emp WHERE salary<(select AVG(salary) from emp)")
print("Salary less than Average Employees : ")
less_avg = cur.fetchall()
for record in less_avg:
    print(record)
cur.execute("SELECT name FROM emp WHERE salary=(select MIN(salary) from emp)")   
less_salary = cur.fetchall()
print("Lowest Salary : ")
print(less_salary)
