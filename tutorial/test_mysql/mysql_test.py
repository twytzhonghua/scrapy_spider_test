import MySQLdb                                             # 导入MySQLdb模块  
  
#db = MySQLdb.connect(host   = 'localhost',                 # 连接到数据库，服务器为本机                    
#                    user   = 'root',                      # 用户名为:root  
#                     passwd = '123',                      # 密码为:1234  
#                     db     = 'gudonginfo')
# 数据库:python  


db=MySQLdb.connect(host='localhost',user='root',passwd='123',port=3306)

cur = db.cursor()  

cur.execute('create database if not exists people_test')
db.select_db('people_test')


cur.execute('create table if not exists people(name varchar(20), age int, info varchar(20))')                  

  
cur.execute('insert into people values("Jee", 21, "F")')   # 执行SQL，添加记录  
cur.execute('insert into people values("Leo", 21, "F")') 
res = cur.execute('delete from people where age=20')       # 执行SQL，删除记录     
db.commit()                                                # 提交事务  
  
res = cur.execute('select * from people')                  # 执行SQL, 获取记录  
res = cur.fetchall()                                       # 获取全部数据  
print(res)                                                 # 打印数据  
cur.close()                                                # 关闭游标  
db.close()            