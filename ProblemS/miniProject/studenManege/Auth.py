import sqlite3
#create a conn connection object
conn = sqlite3.connect("test2.db")
print("opened database successfully")

conn.execute('''CREATE TABLE COMPANY   
            (ID INT PRIMARY KEY   NOT NULL,
            NAME          TEXT    NOT NULL,
            AGE           INT     NOT NULL,
            ADDRESS       CHAR(50),
            SALARY        REAL);''')  # is it nec
print("Table created successfully")  
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
 
conn.commit() # vai easy hai samajh gaya
print("Records created successfully");

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")


# yes we can 
# souze chotolok
print("Operation done successfully");

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
# Can 
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print( "ID = ", row[0])
   print( "NAME = ", row[1])
   print( "ADDRESS = ", row[2])
   print( "SALARY = ", row[3], "\n")

print( "Operation done successfully");
conn.commit()
conn.close()