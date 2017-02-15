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
	
	c = Context({"title": "Django", "user" : person,
		"book_list" : book_list, "today" : today})
	return HttpResponse(t.render(c))
	
def time(request):
	today = datetime.date.today()
	# http://127.0.0.1:8000/blog/time/?id=123
	id = request.GET.get("id")
	name = request.GET.get("name")
	t = loader.get_template("time.html")
	c = Context({"title": "Django", "today" : today, "id" : id, "name" : name})
	return HttpResponse(t.render(c))
	
def foo(request, p1, p2):
	today = datetime.date.today()
	# http://127.0.0.1:8000/blog/time/?id=123
	t = loader.get_template("time.html")
	c = Context({"title": "Django", "today" : today, "id" : p1, "name" : p2})
	return HttpResponse(t.render(c))

def bar(request, id , name):
	today = datetime.date.today()
	# http://127.0.0.1:8000/blog/time/?id=123
	# id = request.GET.get("id")
	name = request.GET.get("name")
	t = loader.get_template("time.html")
	c = Context({"title": "Django", "today" : today, "id" : id, "name" : name})
	return HttpResponse(t.render(c))	
	
