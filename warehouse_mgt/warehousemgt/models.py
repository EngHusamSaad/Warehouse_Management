
from django.db import models
from datetime import datetime
# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='imgs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class User(models.Model):
        photo=models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)
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
    icon = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)
    sn=models.IntegerField()
    isAvailble=models.BooleanField(default=True)
    description=models.TextField()
    sold_date=models.DateField(null=True, blank=True)
    customers = models.ManyToManyField(Customer, related_name="items", blank=True)
    sold_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

        
    
    
