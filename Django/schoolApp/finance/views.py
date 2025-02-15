from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fee(request):
    return HttpResponse("<h1> welcome to finance</h1><h2>fill the application for pay</h2>")

def dues(request):
    return HttpResponse("<h1>show me the dues pending list </h1>")
def financereport(request):
    return HttpResponse("<h1>give me the complete finance list</h1>")