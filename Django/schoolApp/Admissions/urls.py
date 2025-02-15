from django.urls import path
from Admissions.views import addadmission
from Admissions.views import admissionreport

urlpatterns = [
    path('admission/', addadmission),
    path('admissionreport/', admissionreport),
]
