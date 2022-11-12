
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd =""
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE demo_db")





# importing required library
import mysql.connector

# connecting to the database
dataBase = mysql.connector.connect(
					host = "localhost",
					user = "root",
					passwd = "",
					database = "demo_db" )

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE STUDENT (
				NAME VARCHAR(20) NOT NULL,
				BRANCH VARCHAR(50),
				ROLL INT NOT NULL,
				SECTION VARCHAR(5),
				AGE INT
				)"""

# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()




import mysql.connector


mydb = mysql.connector.connect(
host = "localhost",
user = "root",
passwd  = "",
database = "demo_db1"
)

mycursor = mydb.cursor()
sql = "INSERT INTO Student (Name, Branch,Roll,Section,Age) VALUES (%s, %s,%s, %s,%s)"
val = ("Ram", '85',"76543","A","18")

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "details inserted")

# disconnecting from server
mydb.close()






import mysql.connector
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
passwd  = "",
database = "demo_db1"
)
mycursor = mydb.cursor()
sql = "INSERT INTO Student (Name, Branch,Roll,Section,Age) VALUES (%s, %s,%s, %s,%s)"
val = ("Ram", '85',"76543","A","18")

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "details inserted")

# disconnecting from server
mydb.close()






import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="",
database = "demo_db1"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = [("Nikhil", "CSE", "98", "A", "18"),
	("Nisha", "CSE", "99", "A", "18"),
	("Rohan", "MAE", "43", "B", "20"),
	("Amit", "ECE", "24", "A", "21"),
	("Anil", "MAE", "45", "B", "20"),
	("Megha", "ECE", "55", "A", "22"),
	("Sita", "CSE", "95", "A", "19")]

cursorObject.executemany(sql, val)
dataBase.commit()

# disconnecting from server
dataBase.close()