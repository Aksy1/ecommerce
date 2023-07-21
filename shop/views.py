from django.shortcuts import render
from shop.models import Category,Product
def home(request):
    return render(request, 'category.html')
def category(request):
    b = Category.objects.all()
    return render(request,'category.html',{'b':b})
def cloths(request):
    return render(request,'cloths.html')
def allproducts(request,p):
    c=Category.objects.get(slug=p)
    p=Product.objects.filter(category__slug=p)
    return render(request,'products.html',{'p':p,'c':c})
def details(request,p):
    e=Product.objects.get(slug=p)
    return render(request,'details.html',{'e':e})