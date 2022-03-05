from django.contrib import admin

# Register your models here.
from .  models import Product
from .  models import Email
from .  models import Checkout
admin.site.register(Product)
admin.site.register(Email)
admin.site.register(Checkout)