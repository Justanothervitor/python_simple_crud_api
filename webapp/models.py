from django.db import models

class Product(models.Model):
    product_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product_name = models.CharField(max_length=128)
    product_price = models.DecimalField(decimal_places=1,max_digits=7)
    product_description = models.CharField(max_length=255)
    product_vendor = models.CharField(max_length=16)

    def __self__(self):
        return Product



