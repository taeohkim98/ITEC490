import mysql.connector

capstonedb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = capstonedb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
