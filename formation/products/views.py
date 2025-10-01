from django.shortcuts import render
from django.http import HttpResponse


def home(request, *args, **kwargs):
    return render(request, 'indexll.html')

def contact(request):
    return HttpResponse('contact me')
    
def blog(request):
    return HttpResponse('mon blog')