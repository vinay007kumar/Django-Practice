from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'Vinay',
#         'title': 'Blog Post 1',
#         'content' : 'First post content',
#         'date_posted': 'Feb 10, 2022'
#     },
#     {
#         'author': 'Kumar',
#         'title': 'Blog Post 2',
#         'content' : 'Second post content',
#         'date_posted': 'March 10, 2022'
#     }
# ]

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About </h1>')
    return render(request, 'blog/about.html', {'title': 'About'})

