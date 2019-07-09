import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='db_demo_2',autocommit=True)

cursor = connection.cursor()

# query = "insert into users values ('shyam','shyam@gmail.com','shyam1234')"
query = "select * from users"
cursor.execute(query)
data = cursor.fetchall()
print(data)
connection.close()