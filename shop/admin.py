from django.contrib import admin
from shop.models import Category,Product


class Cadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Cadmin)
class Padmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','updated']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,Padmin)