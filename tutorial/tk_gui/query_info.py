import sqlite3
from tkinter import *

class Query_gdinfo(Frame):
	
	def open_db(self):
		pass
		
	def close_db(self):
		self.conn.close()
		pass
		
	def query_name(self):
		print("receive click query button event")
		gudong_name = self.getGudongname()
		print(gudong_name)
		result = []
		t = (gudong_name,)
		#t = ('赵伟',)
		self.c.execute('SELECT * FROM gdinfo WHERE name=?', t)
		all_com = self.c.fetchall()
		
		my_str = ''
		var = StringVar()
		self.label = Label( root, textvariable=var, relief=RAISED )
		if not all_com:
			print("don't find name")
		else:
			#print(all_com)
			for one in all_com:
				#print(one)
				result.append(one)
				#result.append('\n')
				my_str += str(one) + str('\n')
				#my_str = ''.join('\n')
					
		print(result)
		#my_str = '\n'.join(result)
		print(my_str)
		var.set(my_str)
		self.label.pack()
			
		return result


	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.quit

		self.QUIT.pack({"side": "right"})

		self.query = Button(self)
		self.query["text"] = "查询",
		self.query["command"] = self.query_name

		self.query.pack({"side": "left"})

		
	def createText(self):
		self.text = Entry(self.frame, insertwidth = 10)
		self.text.pack()
		
		
	def getGudongname(self):
		gudong_name = self.text.get()
		return gudong_name
		
		
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.conn = sqlite3.connect('../allgdinfo.db')
		self.c = self.conn.cursor()
		self.frame = master
		self.createText()
		self.pack()
		self.createWidgets()

root = Tk()
root.title('查询窗口')  
#center_window(root, 300, 240)  
#root.maxsize(600, 400)  
root.minsize(600, 600) 
#text = Text(root)
app = Query_gdinfo(master=root)
app.mainloop()
root.destroy()






