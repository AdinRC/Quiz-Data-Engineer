import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)

mycursor = connection.cursor()
mycursor.execute("SELECT name FROM customer a LEFT JOIN invoices b ON a.id = b.customer_id WHERE b.customer_id IS NULL")

for connection in mycursor:
    print(connection)