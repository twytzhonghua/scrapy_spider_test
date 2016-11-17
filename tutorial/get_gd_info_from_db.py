import sqlite3

conn = sqlite3.connect('allgdinfo.db')
c = conn.cursor()



t = ('赵伟',)
c.execute('SELECT * FROM gdinfo WHERE name=?', t)
all_com = c.fetchall()
for one in all_com:
    print(one)
    #print('\n')


t = ('红杉资本',)
c.execute('SELECT * FROM gdinfo WHERE name=?', t)
all_com = c.fetchall()
for one in all_com:
    print(one)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
