from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name

class Email(models.Model):
    sr_no=models.AutoField
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50,default="")
    message=models.CharField(max_length=300,default="")

    def __str__(self):
        return self.name

class Checkout(models.Model):
    sr_no=models.AutoField
    items_json=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=300,default="")
    address2=models.CharField(max_length=300,default="")
    city=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    zip=models.CharField(max_length=6)
    phone=models.CharField(max_length=13)

    def __str__(self):
        return self.name
