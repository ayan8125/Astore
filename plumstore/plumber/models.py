from django.db import models
from django.utils import timezone
# Create your models here.
stat = (
    (1,'completed'),
    (0,'InProcess')
)

stat1 = (
    (0,'perday'),
    (1,'fullprocess')
)

stat2 = (
    (0,'without equipments'),
    (1,'with equipments')
)


stat3 = (
    (0,'plumber'),
    (1,'electricians'),
    (2,'repairer')
)

stat4 = (
    (0,'Aborted'),
    (1,'Confirm')
)

class user(models.Model):
    # user_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(max_length=20,primary_key=True,unique=True,default='username')
    password = models.CharField(max_length=25,default="testing321")
    firstname = models.CharField(max_length=25,default="firstname")
    lastname = models.CharField(max_length=25,default="lastname")
    Phonenumber = models.IntegerField(max_length=10,default=7741910761)
    Phonenumber2 = models.IntegerField(max_length=10,default=7741910761)
    email = models.EmailField(max_length=30,default="ayanshaikh7187@gmail.com")
    state = models.CharField(max_length=30,default="state")
    address1 = models.TextField(default="address")
    address12 = models.TextField(default="address")
    city = models.CharField(max_length=30,default="city")
    zipcode = models.IntegerField(default=411042)
    profile = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.firstname


    







