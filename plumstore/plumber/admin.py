from django.contrib import admin
from .models import user
from orders.models import orders
# from employee.models import employee
from hire.models import hire
from employes.models import employes

admin.site.register(user)
admin.site.register(orders)
# admin.site.register(employee)
admin.site.register(employes)
admin.site.register(hire)
# Register your models here.
