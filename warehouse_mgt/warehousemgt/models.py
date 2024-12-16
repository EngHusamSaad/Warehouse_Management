
from django.db import models
from datetime import datetime
import re


# # Create your models here.


class CustomerManger(models.Manager):
    def user_validator(self,formdata):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(formdata["first_name"]) <2:
            errors['first_name']="First name should be at least 2 Chars" 
             
        if len(formdata["second_name"]) <2:
            errors['second_name']="Last Name should be at least 2 Chars"  
                            
        if not formdata["identity"].isdigit() or len(formdata["identity"]) != 9:
            errors['identity'] = "Wrong ID Number!"
        else:
            identity_number = int(formdata["identity"])
            if identity_number < 111111111 or identity_number > 999999999:
                errors['identity'] = "Wrong ID Number!"
            
        if not formdata["identity"].isnumeric():
            errors['identity']="Wrong ID Number should be number !"
            
        if len(formdata["email"]) ==0:
            errors['email']="Should Enter Email !"
            
        
        if Customer.objects.filter(email=formdata["email"]).exists():
            errors["email_exist"]="Email should be uniqe !"
            
        if len(formdata["notes"]) < 10:
            errors['notes']="Notes should be at least 10 Chars"
                   
        
        if not formdata["birthday"] :
            errors["birthday"] = "Filed is Empty Birthday !"
        else:
            str_to_date = datetime.strptime(formdata["birthday"], "%Y-%m-%d").date()
            current_date = datetime.now().date()
           
            if current_date < str_to_date:
                errors["birthday"] = "Birthday should be in the past!"
            
        if not EMAIL_REGEX.match(formdata['email']):                      
            errors['email'] = "Invalid email address!"   
            
        if len(formdata["email"]) ==0 :
            errors['email']="Email Filed is Empty !"
            
        if formdata["password"] != formdata["confirm_password"]  :
            errors['password']="Password Should be Match !"
            
        
        return errors
        
        
        
        
        
        
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
    objects=CustomerManger()
    

class Employee(User):
    postion=models.TextField()
    
class Item(models.Model):
    name_item=models.CharField(max_length=50)
    sn=models.IntegerField()
    isAvailble=models.BooleanField(default=True)
    description=models.TextField()
    sold_date=models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name="items", blank=True,on_delete=models.CASCADE,null=True)
    icon = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)