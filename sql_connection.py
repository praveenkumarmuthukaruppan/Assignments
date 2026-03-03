import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="praveen93",
  database="classicmodels"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT lastName,firstName FROM employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("CREATE TABLE employees1 (lastname VARCHAR(255), firstname VARCHAR(255))")
sql = "INSERT INTO employees1 (lastname,firstname) VALUES (%s, %s)"

mycursor.executemany(sql, myresult)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
