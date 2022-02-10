from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home </h1>')
def home1(request):
    return HttpResponse('<h1>Blog Home1 </h1>')
def about(request):
    return HttpResponse('<h1>Blog About </h1>')
