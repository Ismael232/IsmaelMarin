import sqlite3
conexion = sqlite3.connect('base.db')
cur = conexion.cursor()

def createTable(tabla):
    cur.execute(f"CREATE TABLE IF NOT EXISTS {tabla} (id INTERGER, USERNAME TEXT, TELF TEXT)")
    conexion.commit()

def insertData(id,user,telf,tabla):
    cur.execute(f"insert into {tabla} values (?,?,?)",(id,user,telf))
    conexion.commit()

def showTable(tabla):
    cur.execute(f"select * from {tabla}")
    datos = cur.fetchall()
    return  datos


def insertDataToBase(nombreTabla,dataframe):
    dataframe.to_sql(nombreTabla,conexion,if_exists = 'replace', index = False)
    conexion.commit()
