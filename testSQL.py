import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "rpms")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

sql_getTableList = "SELECT information_schema.`TABLES`.TABLE_NAME " \
                   "FROM information_schema.`TABLES` " \
                   "WHERE information_schema.`TABLES`.TABLE_SCHEMA = 'rpms'"
tableList = []
try:
    cursor.execute(sql_getTableList)
    result = cursor.fetchall()

    for tname in result:
        tableList.append(str(tname)[2:-3])
    # print(tableList)
except:
   print ("Error: unable to fetch data")



# 关闭数据库连接
db.close()
