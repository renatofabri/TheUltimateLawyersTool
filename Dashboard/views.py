'''
Created on Oct 18, 2014

@author: renato
'''
from django.http.response import HttpResponse

def home(request):
    return HttpResponse("Hello World")