a = 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\_MEI66~1\\scrapy\\VERSION'
b = a.strip('\\').replace('\\', ' ').split(' ')
print b[-1]