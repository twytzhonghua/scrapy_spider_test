import urllib

class GetStockNumber:
	def __init__(self, name):
		self.name = name
	
	def getHtml(self,url):
		page = urllib.urlopen(url)
		html = page.read()
		return html

	def getnumbers2store(self):
		html1 = self.getHtml("http://www.caiguu.com/shichang/jujiao/91582_2.html")
		#html2 = html1.decode('utf-8')
		with open('sh.html', 'wb') as f:
			f.write(html1)


getStock = GetStockNumber('zh')
getStock.getnumbers2store()
