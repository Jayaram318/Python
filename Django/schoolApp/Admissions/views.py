from django.shortcuts import render


# Create your views here.
# function based views
def addadmission(request):
    return render(request, 'Admissions/addadmission.html')
def admissionreport(request):
    return render(request, 'Admissions/admissionreport.html')