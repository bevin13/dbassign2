import sqlite3
con = sqlite3.connect('employee.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS EMPLOYEE ")
emp = """CREATE TABLE EMPLOYEE(
         EMP_name CHAR(20) NOT NULL, 
         EMP_id INTEGER NOT NULL,
         EMP_salary INTEGER NOT NULL,
         Department_id INTEGER NOT NULL)"""
cur.execute(emp)

addColumn = "ALTER TABLE EMPLOYEE ADD COLUMN CITY VARCHAR(20)"
cur.execute (addColumn)

con.execute("INSERT  INTO EMPLOYEE (EMP_name,EMP_id,EMP_salary,Department_id,CITY) " 
                 "VALUES ('George',1,20000,102,'NewYork')")
con.execute("INSERT  INTO EMPLOYEE (EMP_name,EMP_id,EMP_salary,Department_id,CITY) " 
                 "VALUES ('Malik',2,25000,105,'Berlin')")
con.execute("INSERT  INTO EMPLOYEE (EMP_name,EMP_id,EMP_salary,Department_id,CITY) " 
                 "VALUES ('Naomi',3,30000,201,'London')")
con.execute("INSERT  INTO EMPLOYEE (EMP_name,EMP_id,EMP_salary,Department_id,CITY) " 
                 "VALUES ('Paul',4,28000,307,'Poland')")
con.execute("INSERT  INTO EMPLOYEE (EMP_name,EMP_id,EMP_salary,Department_id,CITY) " 
                 "VALUES ('Donnel',5,35000,305,'Paris')")
con.commit()

cur1 = con.execute("SELECT EMP_name,EMP_id,EMP_salary from EMPLOYEE")
print(cur1.fetchall())

a = input("Enter the alphabet : ")
cur2 = con.execute("SELECT * from EMPLOYEE where upper(EMP_name) LIKE'"+ a +"%'")
print(cur2.fetchall())

d = input("Enter the Employee ID : ")
cur3 = con.execute("SELECT * FROM EMPLOYEE where EMP_id = "+ d + "")
print(cur3.fetchall())

j = input("Enter the id of employee whose name you want to change : ")
q = input("Enter new employee name : ")
cur4 = con.execute("UPDATE EMPLOYEE SET EMP_name = '"+ q +"'where EMP_id = '"+ j +"'")
cur = con.execute("SELECT * from EMPLOYEE")
print(cur.fetchall())

cur5 = con.cursor()
cur5.execute("DROP TABLE IF EXISTS DEPARTMENTS ")
dep = """CREATE TABLE DEPARTMENTS(
         Department_id INTEGER NOT NULL,
         Department_name CHAR(20) NOT NULL)"""
cur5.execute(dep)

con.execute("INSERT  INTO DEPARTMENTS (Department_id,Department_name) " 
                 "VALUES (102,'Front-end')")
con.execute("INSERT  INTO DEPARTMENTS (Department_id,Department_name) " 
                 "VALUES (105,'Back-end')")
con.execute("INSERT  INTO DEPARTMENTS (Department_id,Department_name) " 
                 "VALUES (201,'Full-stack')")
con.execute("INSERT  INTO DEPARTMENTS (Department_id,Department_name) " 
                 "VALUES (307,'App Developement')")
con.execute("INSERT  INTO DEPARTMENTS (Department_id,Department_name) " 
                 "VALUES (305,'Game Developement')")
con.commit()
cur5.execute("SELECT * from DEPARTMENTS")
print(cur5.fetchall())

n = input("Enter the Department ID : ")
print(con.execute("Select EMP_name,EMP_id,EMP_salary,EMPLOYEE.Department_id,CITY,Department_name from EMPLOYEE,DEPARTMENTS where EMPLOYEE.Department_id== '"+ n +"' and DEPARTMENTS.Department_id== '"+ n +"'" ).fetchall())

con.close()
