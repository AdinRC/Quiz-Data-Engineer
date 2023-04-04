import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)
mycursor = connection.cursor()

# create table customer, invoices, invoice_lines
mycursor.execute("CREATE TABLE customer (id INTEGER NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, tel VARCHAR(255) NOT NULL, created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL, PRIMARY KEY (id))")
mycursor.execute("CREATE TABLE invoices (id INTEGER NOT NULL AUTO_INCREMENT, number INTEGER NOT NULL, sub_total DOUBLE NOT NULL, tax_total DOUBLE NOT NULL, total DOUBLE NOT NULL, customer_id INTEGER NOT NULL, created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customer (id))")
mycursor.execute("CREATE TABLE invoice_lines (id INTEGER NOT NULL AUTO_INCREMENT, description VARCHAR(255) NOT NULL, unit_price DOUBLE NOT NULL, quantity INTEGER NOT NULL,sub_total DOUBLE NOT NULL,  tax_total DOUBLE NOT NULL, total DOUBLE NOT NULL, tax_id INTEGER NULL, sku_id INTEGER NOT NULL, invoice_id INTEGER NOT NULL, PRIMARY KEY (id), FOREIGN KEY (invoice_id) REFERENCES invoices (id))")
