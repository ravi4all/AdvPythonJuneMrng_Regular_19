import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='db_demo_2',autocommit=True)

cursor = connection.cursor()
name = 'Raman'
email = 'raman@gmail.com'
pwd = 'raman1212'
query = "insert into users values (%s,%s,%s)"
cursor.execute(query, (name,email,pwd))
data = cursor.fetchall()
print(data)
connection.close()