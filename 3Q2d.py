import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)

mycursor = connection.cursor()
mycursor.execute("SELECT c.name, il.description, il.unit_price, il.quantity FROM customer c JOIN invoices i ON c.id = i.customer_id JOIN invoice_lines il ON i.id = il.invoice_id")

print ("customer name, book name, price, quantity")
for connection in mycursor:
    print(connection)