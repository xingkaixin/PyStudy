import MySQLdb


conn = MySQLdb.connect(host='localhost',user='root',passwd='inter1314',db='test')
cursor = conn.cursor()
cursor.execute("select * from note")
print cursor.rowcount