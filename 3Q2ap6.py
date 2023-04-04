import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)

mycursor = connection.cursor()

# insert many data into table invoice_lines
sql = "INSERT INTO invoice_lines (id, description, unit_price, quantity, sub_total, tax_total, total, sku_id, invoice_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    (1, 'Book #1', '30', '1', '30', '0', '30', '1', '1'),
    (2, 'Book #2', '25', '4', '100', '0', '100', '2', '2'),
    (3, 'Book #3', '50', '1', '50', '0', '50', '3', '2'),
    (4, 'Book #1', '30', '1', '30', '0', '30', '1', '3'),
    (5, 'Book #1', '30', '1', '30', '0', '30', '1', '4'),
    (6, 'Book #2', '25', '1', '25', '0', '25', '2', '4'),
    (7, 'Book #1', '30', '5', '150', '0', '150', '1','5'),
    (8, 'Book #3', '50', '6', '300', '0', '300', '3', '5')
]
mycursor.executemany(sql, val)
connection.commit()
print(mycursor.rowcount, "record inserted.")