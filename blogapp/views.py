from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post, Category

# Create your views here.
def index(request):
    data = Post.objects.order_by('-id')
    return render(request, 'blogapp/home.html' , {"posts" : data})

def single_post(request, id):
    data = Post.objects.get(id=id)
    return render(request, 'blogapp/single_post.html' , {"post" : data})
