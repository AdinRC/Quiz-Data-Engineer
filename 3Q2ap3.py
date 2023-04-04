import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)

mycursor = connection.cursor()

# insert 1 data into table customer
sql = "INSERT INTO customer (id, name, email, tel, created_at, updated_at) VALUES (%s, %s,%s, %s,%s, %s)"
val = ("1", "Irfan Bakti", "irfan88@example.com", "+60123456789", "2019-08-07 08:13:21", "2019-08-07 08:13:21")
mycursor.execute(sql, val)
connection.commit()
print(mycursor.rowcount, "record inserted.")