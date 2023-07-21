from django.contrib import admin
from cart.models import Cart,Order,Account

# class Cartadmin(admin.ModelAdmin):
#     list_display = ['products.name','user.username']
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Account)
