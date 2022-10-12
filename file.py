import mysql.connector as c

con=c.connect(
    host='localhost',
    user='root',
    password='Admin@123',
    database='student'
)

cursor = con.cursor()

# id = int(input("ID : "))
# name = input("Name : ")
# age = int(input("Age : "))
# city = input("City : ")

# query="Insert into testcode values({}, '{}',{}, '{}')".format(id, name, age, city)
query = "SELECT*FROM testcode"
cursor.execute(query)
# con.commit()

# print("Data inserted successfully...")
print("executed...")