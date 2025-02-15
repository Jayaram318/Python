from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based views
def addadmission(request):
    return HttpResponse("<h1> This is the admission page </h1> <h2> welcome to the school </h2>")
def addadmissionreport(request):
    return HttpResponse("<h1> This is the report page </h1> <h2> welcome to the school </h2>")