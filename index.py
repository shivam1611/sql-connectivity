#  STEP 1: importing the module 
import mysql.connector as sql_connector

# connecting to the database and return the database object 
# connect() method will return the  database Object 

# STEP 2: Establishing the connection 
my_connection = sql_connector.connect(host="localhost",user='root',password='root')
# heremy_connection is my data base object 
# now prepare a cursor object 

# STEP 3: Preparing the cursor object 
cursor = my_connection.cursor()

#STEP 4: Varifying whether the connection established or not ??

if my_connection.is_connected():
    print("Connection Established!!")

# Executing the SQL queries with the help of cursor object 
# execute()method is used to execute the sql queires in DB 

cursor.execute('use class;')
cursor.execute(
    "INSERT into classData values ('%s',%s,%s,%s,'%s');"
    %
    ('Palki',5,400,500,'B')
    )

# my_connection.commit() # Save the entries permanently 
cursor.execute('select * from classData')
# Now the whole table is returned from the database, Now we also have some methods to  manipulate the data 

data = cursor.fetchall() 
count = cursor.rowcount
print(count)

for i in range(len(data)):
    print(data[i])


# just like the file handling, we close the file after the operation performed here too, we will disconnect the database after performing the task
my_connection.close()
