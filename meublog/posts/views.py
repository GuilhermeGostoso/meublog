from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
	posts = Post.objects.all().order_by('Create_date')
	return render(request, 'blog.html', {'posts' : posts})
# Create your views here.
