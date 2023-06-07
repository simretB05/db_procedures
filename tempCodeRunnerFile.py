import dbcreds
import mariadb
conn=mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()
cursor.execute('CALL new_db_procedure()')
result=cursor.fetchall()
cursor.close()
conn.close()