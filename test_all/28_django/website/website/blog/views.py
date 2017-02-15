from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
import datetime

# Create your views here.

class Person(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
	
	def say(self):
		return 'my name is ' + self.name


def index(request):
	t = loader.get_template('index.html')
	user1 = {"name" : "tom", "age" : 23, "sex" : "male"}
	
	person = Person("jack", 16, 'woman')
	
	book_list = ['python', 'ruby', 'java', 'c']
	today = datetime.date.today()
	# book_list2 = []
	# for book in book_list:
		# book_list2.append(book.upper())
	
	c = Context({"title": "Django", "user" : person,
		"book_list" : book_list, "today" : today})
	return HttpResponse(t.render(c))
	
def time(request):
	today = datetime.date.today()
	id = request.GET.get("id")
	t = loader.get_template("time.html")
	c = Context({"title": "Django", "today" : today})
	return HttpResponse(t.render(c))
	
