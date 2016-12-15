# -*- coding: utf-8 -*-

import MySQLdb

def init_mysql_gudong_data_base():
    db = MySQLdb.connect(host='localhost',user='root',passwd='123',port=3306, charset="utf8")
    cur = db.cursor()  
    cur.execute('create database if not exists yidian_gudonginfo')
    db.select_db('yidian_gudonginfo')
    db.set_character_set('utf8')
    cur.execute('SET NAMES utf8;') 
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    cur.execute('create table if not exists gudonginfo (gudong_name varchar(40), date varchar(20), stock_name varchar(20),stock_number varchar(20), percent varchar(20), hold_num varchar(20), increase varchar(20), stock_type varchar(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')
    db.commit()  
    db.close()
    
def yidian_store_gudong_db(all_info):
    db = MySQLdb.connect(host='localhost',user='root',passwd='123',port=3306, charset="utf8")
    db.select_db('yidian_gudonginfo')
    db.set_character_set('utf8')   
    cur = db.cursor()      
    cur.executemany("insert into gudonginfo values (%s,%s,%s,%s,%s,%s,%s,%s)", all_info)
    db.commit()
    cur.close()
    db.close()

def yidian_query_gudong_name(name):
    t = name
    print('enter yidian_query_gudong_name')
    print(name)
    db = MySQLdb.connect(host='localhost',user='root',passwd='123',port=3306, charset="utf8")
    db.select_db('yidian_gudonginfo')
    cur = db.cursor()
    cur.execute("SELECT * FROM gudonginfo WHERE gudong_name='%s' " % t)
    #db.commit()  
    
    all_ret = cur.fetchall()
    
    #print(all_ret)
    cur.close()
    db.close()
    return all_ret
    