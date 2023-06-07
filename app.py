import dbcreds
import mariadb
conn=mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()
cursor.execute("CALL new_db_procedure('client109','eamil@gmai8000098.com','123488856street 1299845ave')")
result=cursor.fetchall()

cursor.close()
conn.close() 



