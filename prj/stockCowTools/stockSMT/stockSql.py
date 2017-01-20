# -*- coding: utf-8 -*-

import MySQLdb

def init_mysql_gudong_data_base():
    print('begint init_mysql_gudong_data_base')
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    cur = db.cursor()  
    cur.execute('create database if not exists ltgudongdb')
    db.select_db('ltgudongdb')
    db.set_character_set('utf8')
    cur.execute('SET NAMES utf8;') 
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    cur.execute('create table if not exists LTgudonginfo (stock_number varchar(20), cname varchar(20),gudong_name varchar(100), hold_num varchar(20), percent varchar(20), ichange varchar(20), date varchar(20), stock_type varchar(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')
    cur.execute('create table if not exists LTgudongNumber (stock_number varchar(20), cname varchar(20),number varchar(20), ichange_percent varchar(20), date varchar(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')
    db.close()
    

def init_mysql_old_gudong_data_base():
    print('begint init_mysql_gudong_data_base')
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    cur = db.cursor()  
    cur.execute('create database if not exists old_ltgudongdb')
    db.select_db('old_ltgudongdb')
    db.set_character_set('utf8')
    cur.execute('SET NAMES utf8;') 
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    cur.execute('create table if not exists LTgudonginfo (stock_number varchar(20), cname varchar(20),gudong_name varchar(100), hold_num varchar(20), percent varchar(20), ichange varchar(20), date varchar(20), stock_type varchar(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')
    cur.execute('create table if not exists LTgudongNumber (stock_number varchar(20), cname varchar(20),number varchar(20), ichange_percent varchar(20), date varchar(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')
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
	
def store_old_lt_gudong_db(all_info):
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    db.select_db('old_ltgudongdb')
    db.set_character_set('utf8')   
    cur = db.cursor()      
    cur.executemany("insert into LTgudonginfo values (%s,%s,%s,%s,%s,%s,%s,%s)", all_info)
    db.commit()
    cur.close()
    db.close()

def store_lt_gudong_num_db(all_info):
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    db.select_db('ltgudongdb')
    db.set_character_set('utf8')   
    cur = db.cursor()      
    cur.executemany("insert into LTgudongNumber values (%s,%s,%s,%s,%s)", all_info)
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
    db.commit()  
    
    all_ret = cur.fetchall()
    
    #print(all_ret)
    cur.close()
    db.close()
    return all_ret

def query_lt_gudong_info_exist(stock_num, date):
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',port=3306, charset="utf8")
    db.select_db('ltgudongdb')
    query_cmd = 'SELECT * FROM LTgudonginfo WHERE stock_number = %s and date=%s' % (stock_num, date)
    cur = db.cursor()
    cur.execute(query_cmd)
    db.commit()
    ret =  cur.fetchall()
    if ret:
        print(ret)
    cur.close()
    db.close()
    return ret
    
    