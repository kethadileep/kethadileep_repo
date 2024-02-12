from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer


class Telecom_Customers(generics.ListCreateAPIView):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer