import pymysql
import shutil

#
#
# 已经建好数据库，完成创建表
#
# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "rpms")
print("success: connected to db")
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
    print("success: get table name list")
except:
    print("Error: unable to fetch data")

print(len(tableList))
# 对每一张表进行如下操作
# 分离表空间
# 覆盖数据文件.ibd
# 导入表空间
basedir = "D:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\rpms_nky\\"
targetdir = "D:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\rpms\\"
for tname in tableList:
    print("table name: " + tname)
    try:
        sql_DISCARD = "ALTER TABLE " + tname + " DISCARD TABLESPACE;"
        cursor.execute(sql_DISCARD)
        print(" " + sql_DISCARD)
    except:
        print("Error: DISCARD")

    try:
        shutil.copyfile(basedir + tname + ".ibd", targetdir + tname + ".ibd")
        print(" " + basedir + tname + ".ibd", targetdir + tname + ".ibd")
    except:
        print("Error: move")

    try:
        sql_IMPORT = "ALTER TABLE " + tname + " IMPORT TABLESPACE;"
        cursor.execute(sql_IMPORT)
        print(" " + sql_IMPORT)
    except:
        print("Error: IMPORT")



# 关闭数据库连接
db.close()
