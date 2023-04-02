import sqlite3
conexion = sqlite3.connect('base.db')
cur = conexion.cursor()

def createTable():
    cur.execute("CREATE TABLE IF NOT EXISTS USER (id INTERGER, USERNAME TEXT, EMAIL TEXT)")
    conexion.commit()

def insertData(id,user,email):
    cur.execute("insert into user values (?,?,?)",(id,user,email))
    conexion.commit()

def showTable():
    cur.execute("select * from USER")
