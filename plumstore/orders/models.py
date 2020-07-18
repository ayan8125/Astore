from django.db import models
from plumber.models import user
# from employee.models import employee
from employes.models import employes
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



class orders(models.Model):
    order_id = models.AutoField(primary_key=True,default="username")
    product = models.CharField(max_length=30,default="product")
    order_date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(null=True,max_length=50,choices=stat)
    days = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    product_type = models.IntegerField(null=True,max_length=50,choices=stat1)
    order_type = models.IntegerField(null=True,max_length=50,choices=stat2)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class order_detail(models.Model):
    orders = models.ForeignKey(orders, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    employes = models.ForeignKey(employes, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    totol_cost = models.FloatField()
    profit = models.FloatField()
    noemp = models.IntegerField(default=0)


    def __str__(self):
        return self.orders.product
    
