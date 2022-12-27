import mysql.connector

mydb = mysql.connector.connect(
  host="Logice",
  user="LogiceAdmin",
  password="Wlsghqudtls!"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
