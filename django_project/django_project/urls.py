from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django_app.views import *




urlpatterns = [
   path('customers/', Telecom_Customers.as_view(), name='Telecom_customer_data'),
]
