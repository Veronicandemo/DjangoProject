from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField( max_length=50, blank=True, null=True)
#   last_name,
    last_name = models.CharField( max_length=50, blank=True, null=True)
#   age,
    age = models.IntegerField( blank=True, null=True)
#   country,
    country = models.CharField(max_length=150, blank=True, null=True)
#   phone_number
    phone_number = models.CharField(max_length=50, blank=True, null=True)
#   area of residence
    residence_area = models.CharField( max_length=50, blank=True, null=True)
#   position
    role = models.CharField( max_length=50, blank=True, null=True)
#   email,
    email= models.EmailField(max_length=254)
#   gender,
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O', 'Other'),
    )
    gender =models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    
class Student(models.Model):  
    first_name = models.CharField( max_length=50, null=True)
    last_name = models.CharField( max_length=50, null=True) 
    age = models.IntegerField( blank=True, null=True)
    residential_area = models.CharField( max_length=50,null=True)
    LAB_CHOICES = (
        ('AnitaB Lab', "AnitaB Lab"),
        ('Ada Lab', "Ada Lab"),
        ('Hopper Lab', "Hopper Lab"),
    )
    lab =models.CharField(max_length=254,choices=LAB_CHOICES,null=True)
    COUNTRY_CHOICES = (
        ('Kenya',"Kenya"),
        ('Uganda',"Uganda"),
        ('Rwanda', "Rwanda"),
        ('Tanzania', "Tanzania")
    )
    countries = models.CharField(max_length=254, choices = COUNTRY_CHOICES, null=True)
    