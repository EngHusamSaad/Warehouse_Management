from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
        photo=models.TextField()
        first_name=models.CharField(max_length=50)
        second_name=models.CharField(max_length=50)
        identity=models.IntegerField()
        email=models.EmailField(max_length=254)
        password=models.TextField()
        birthday=models.DateField()
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)

        def __str__(self):
          return f"{self.first_name} {self.second_name}"  
    
class Customer(User):
    notes=models.TextField()
    

class Employee(User):
    postion=models.TextField()
    
class Item(models.Model):
    name_item=models.CharField(max_length=50)
    icon=models.TextField()
    sn=models.IntegerField()
    isAvailble=models.BooleanField()
    description=models.TextField()
    sold_date=models.DateField()
    customers=models.ManyToManyField(Customer,related_name="Items")
    sold_by=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
