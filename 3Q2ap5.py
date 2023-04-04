import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)

mycursor = connection.cursor()
# insert many data into table invoices
sql = "INSERT INTO invoices (id, number, sub_total, tax_total, total, customer_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    (1, '20190001', '30', '0', '30', '1', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
    (2, '20190002', '150', '0', '150', '2', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
    (3, '20190003', '30', '0', '30', '2', '2019-09-15 08:13:21', '2019-09-15 08:13:21'),
    (4, '20190004', '55', '0', '55', '3', '2019-09-15 08:13:21', '2019-09-15 08:13:21'),
    (5, '20190005', '450', '0', '0', '6', '2019-09-15 08:13:21', '2019-09-15 08:13:21')
]
mycursor.executemany(sql, val)
connection.commit()
print(mycursor.rowcount, "record inserted.")