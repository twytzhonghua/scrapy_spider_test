# -*- coding: utf-8 -*-

import MySQLdb

def init_mysql_gudong_data_base():
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    cur = db.cursor()  
    cur.execute('create database if not exists ltgudongdb')
    db.select_db('ltgudongdb')
    db.set_character_set('utf8')
    cur.execute('SET NAMES utf8;') 
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    cur.execute('create table if not exists LTgudonginfo (stock_number varchar(20), cname varchar(20),gudong_name varchar(100), hold_num varchar(20), percent varchar(20), ichange varchar(20), date varchar(20), stock_type varchar(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')
    db.close()
    
	
	
def store_lt_gudong_db(all_info):
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    db.select_db('ltgudongdb')
    db.set_character_set('utf8')   
    cur = db.cursor()      
    cur.executemany("insert into LTgudonginfo values (%s,%s,%s,%s,%s,%s,%s,%s)", all_info)
    db.commit()
    cur.close()
    db.close()

	
	
def query_lt_gudong_name(name):
    t = name
    print('enter query_lt_gudong_name = ', name)
    #print(name)
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    db.select_db('ltgudongdb')
    cur = db.cursor()
    cur.execute("SELECT * FROM LTgudonginfo WHERE gudong_name='%s' " % t)
    #db.commit()  
    
    all_ret = cur.fetchall()
    
    #print(all_ret)
    cur.close()
    db.close()
    return all_ret
    