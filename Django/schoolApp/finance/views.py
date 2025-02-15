from django.shortcuts import render

# Create your views here.

def fee(request):
    return render(request, 'finance/fee.html')

def dues(request):
    return render(request, 'finance/dues.html')
def financereport(request):
    return render(request, 'finance/financereport.html')