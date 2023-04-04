# Ini adalah keseluruhan, lebih mudah tengok part by part

import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)
mycursor = connection.cursor()

# create database
#mycursor.execute("CREATE DATABASE testdatabse")


# create table customer, invoices, invoice_lines
#mycursor.execute("CREATE TABLE customer (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, tel VARCHAR(255) NOT NULL, created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL, PRIMARY KEY (id))")
#mycursor.execute("CREATE TABLE invoices (id INTEGER NOT NULL AUTO_INCREMENT, number INTEGER NOT NULL, sub_total DOUBLE NOT NULL, tax_total DOUBLE NOT NULL, total DOUBLE NOT NULL, customer_id INTEGER NOT NULL, created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customer (id))")
#mycursor.execute("CREATE TABLE invoice_lines (id INTEGER NOT NULL AUTO_INCREMENT, description VARCHAR(255) NOT NULL, unit_price DOUBLE NOT NULL, quantity INTEGER NOT NULL,sub_total DOUBLE NOT NULL,  tax_total DOUBLE NOT NULL, total DOUBLE NOT NULL, tax_id INTEGER NULL, sku_id INTEGER NOT NULL, invoice_id INTEGER NOT NULL, PRIMARY KEY (id), FOREIGN KEY (invoice_id) REFERENCES invoices (id))")


# insert 1 data into table customer
#sql = "INSERT INTO customer (id, name, email, tel, created_at, updated_at) VALUES (%s, %s,%s, %s,%s, %s)"
#val = ("1", "Irfan Bakti", "irfan88@example.com", "+60123456789", "2019-08-07 08:13:21", "2019-08-07 08:13:21")
#mycursor.execute(sql, val)
#connection.commit()
#print(mycursor.rowcount, "record inserted.")


# insert many data into table customer
#sql = "INSERT INTO customer (id, name, email, tel, created_at, updated_at) VALUES (%s, %s,%s, %s,%s, %s)"
#val = [
#    (2, 'Jack Smmith', 'jack.smmith@acme.io', '+60132456781', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
#    (3, 'Nazir', '', '+601185434012', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
#    (4, 'Faiz Ma', 'faiz.ma@jholow.cn', '+6019772002', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
#    (5, 'Isham Rais', 'isham@pmo.gov.my', '+60135482020', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
#    (6, 'Shanon Teoh', 'shahnon.teoh@st.com.sg', '', '2019-08-07 08:13:21', '2019-08-07 08:13:21')
#]
#mycursor.executemany(sql, val)
#connection.commit()
#print(mycursor.rowcount, "record inserted.")


# insert many data into table invoices
#sql = "INSERT INTO invoices (id, number, sub_total, tax_total, total, customer_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#val = [
#    (1, '20190001', '30', '0', '30', '1', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
#    (2, '20190002', '150', '0', '150', '2', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
#    (3, '20190003', '30', '0', '30', '2', '2019-09-15 08:13:21', '2019-09-15 08:13:21'),
#    (4, '20190004', '55', '0', '55', '3', '2019-09-15 08:13:21', '2019-09-15 08:13:21'),
#    (5, '20190005', '450', '0', '0', '6', '2019-09-15 08:13:21', '2019-09-15 08:13:21')
#]
#mycursor.executemany(sql, val)
#connection.commit()
#print(mycursor.rowcount, "record inserted.")


# insert many data into table invoice_lines
#sql = "INSERT INTO invoice_lines (id, description, unit_price, quantity, sub_total, tax_total, total, sku_id, invoice_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#val = [
#    (1, 'Book #1', '30', '1', '30', '0', '30', '1', '1'),
#    (2, 'Book #2', '25', '4', '100', '0', '100', '2', '2'),
#    (3, 'Book #3', '50', '1', '50', '0', '50', '3', '2'),
#    (4, 'Book #1', '30', '1', '30', '0', '30', '1', '3'),
#    (5, 'Book #1', '30', '1', '30', '0', '30', '1', '4'),
#    (6, 'Book #2', '25', '1', '25', '0', '25', '2', '4'),
#    (7, 'Book #1', '30', '5', '150', '0', '150', '1','5'),
#    (8, 'Book #3', '50', '6', '300', '0', '300', '3', '5')
#]
#mycursor.executemany(sql, val)
#connection.commit()
#print(mycursor.rowcount, "record inserted.")

