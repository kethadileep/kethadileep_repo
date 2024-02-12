from django.db import models


class Customer(models.Model):
   name = models.CharField(max_length=255)
   dob = models.DateField()
   email = models.EmailField()
   adhar_number = models.CharField(max_length=12)
   registration_date = models.DateField()
   mobile_number = models.CharField(max_length=10)


   def __str__(self):
       return self.name