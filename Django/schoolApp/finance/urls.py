from django.urls import path
from finance.views import fee
from finance.views import dues
from finance.views import financereport

urlpatterns = [ 
    path('fee/', fee),
    path('dues/', dues),
    path('financereport/', financereport),
]
