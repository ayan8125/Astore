from django.db import models
from plumber.models import user
from django.utils import timezone
# Create your models here.

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


class hire(models.Model):
    hire_id = models.AutoField(primary_key=True)
    hire_product = models.CharField(max_length=50)
    hire_status = models.IntegerField(max_length=50,choices=stat4)
    hire_type = models.IntegerField(max_length=50,choices=stat2)
    hire_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.firstname

    def give_icon(self):
        if self.hire_product.lower() == 'plumber':
            return 'shower'
        if self.hire_product.lower() == 'electricians':
            return 'charging-station'
        if self.hire_product.lower() == 'television screen':
            return 'tv'
        if self.hire_product.lower() == 'washing machine':
            return 'tint'
        if self.hire_product.lower() == 'motor':
            return 'tint'
    def give_product(self):
        if self.hire_product.lower() is 'plumber' or self.hire_product.lower() is 'electricians':
            return self.hire_product
        if self.hire_product.lower() == 'television screen':
            return 'television screen Repairer'
        if self.hire_product.lower() == 'washing machine':
            return 'washing machine Repairer'
        if self.hire_product.lower() == 'motor':
            return 'water motor Repairer'