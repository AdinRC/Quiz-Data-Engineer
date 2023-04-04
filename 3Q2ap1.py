import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
)

mycursor = connection.cursor()
# create database
mycursor.execute("CREATE DATABASE testdatabse")