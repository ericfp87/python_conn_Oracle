import cx_Oracle
import pandas as pd

tns_entry = cx_Oracle.makedsn(
    'dbconnect.megaerp.online', 
    '4221', 
    service_name='xepdb1'  
)

username = 'xxx'
password = 'xxx'

try:
    connection = cx_Oracle.connect(username, password, tns_entry)

    cursor = connection.cursor()

    cursor.execute("select * from MEGA.con_centro_custo@EMGD")
    columns = [col[0] for col in cursor.description]
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=columns)
    print(df)

    
    
    cursor.close()
    connection.close()
except cx_Oracle.Error as error:
    print("Erro ao conectar ao banco de dados:", error)
