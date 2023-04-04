import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabse"
)

mycursor = connection.cursor()
# insert many data into table customer
sql = "INSERT INTO customer (id, name, email, tel, created_at, updated_at) VALUES (%s, %s,%s, %s,%s, %s)"
val = [
    (2, 'Jack Smmith', 'jack.smmith@acme.io', '+60132456781', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
    (3, 'Nazir', '', '+601185434012', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
    (4, 'Faiz Ma', 'faiz.ma@jholow.cn', '+6019772002', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
    (5, 'Isham Rais', 'isham@pmo.gov.my', '+60135482020', '2019-08-07 08:13:21', '2019-08-07 08:13:21'),
    (6, 'Shanon Teoh', 'shahnon.teoh@st.com.sg', '', '2019-08-07 08:13:21', '2019-08-07 08:13:21')
]
mycursor.executemany(sql, val)
connection.commit()
print(mycursor.rowcount, "record inserted.")