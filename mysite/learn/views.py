#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from learn.models import Article
from datetime import datetime

def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
	
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
	
'''
def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})
'''

# Create your views here.
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})
	
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})