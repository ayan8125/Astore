from django.db import models

import datetime
# Create your models here.
choice = (
    ('plumber','plumber'),
    ('electricians','electricians'),
    ('repairer','repairer')
)

class employes(models.Model):
    username = models.CharField(primary_key=True,max_length=20,default="username")
    password = models.CharField(default='password',max_length=50)
    firstname = models.CharField(null=True,max_length=50,default="firstname")
    lastname = models.CharField(null=True,max_length=50,default="lastname")
    work = models.CharField(null=True,max_length=50,choices=choice,default="work")
    Phonenumber = models.IntegerField(max_length=10,default=7741910761,)
    Phonenumber2 = models.IntegerField(max_length=10,default=7741910761)
    email = models.EmailField(max_length=30,default="ayanshaikh7187@gmail.com")
    state = models.CharField(max_length=30,default="state")
    address1 = models.TextField(default="address")
    address2 = models.TextField(default="address")
    city = models.CharField(max_length=30,default="city")
    zipcode = models.IntegerField(default=411042)
    dob = models.DateField(null=True)
    age = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)
    addharno = models.IntegerField(default=0)
    adharimage = models.ImageField(default='default.jpg', upload_to='adhar_pics')
    profile = models.ImageField(default='default.jpg', upload_to='emp_pics')

    
    def __str__(self):
        return f"{self.firstname} , {self.work}"
        
    def give_age(self):
        day = datetime.datetime.now().strftime("%Y")
        day2 = self.dob.strftime("%Y")
        return  int(day) - int(day2)
