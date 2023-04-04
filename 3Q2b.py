import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)

mycursor = connection.cursor()
mycursor.execute("SELECT customer_id FROM invoices INNER JOIN invoice_lines ON invoices.id = invoice_lines.invoice_id GROUP BY customer_id HAVING SUM(quantity) > 5")

for connection in mycursor:
    print(connection)