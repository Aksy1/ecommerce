from django.shortcuts import render,redirect
from shop.models import Product
from cart.models import Cart,Account,Order
from django.contrib.auth.decorators import login_required
@login_required
def add_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity+=1
        cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(products=product,user=user,quantity=1)
        cart.save()
    return redirect('cart:cartview')
@login_required
def cartview(request):
    total=0
    user=request.user
    try:
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity*i.products.price

    except Cart.DoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart,'total':total})

@login_required
def add_remove(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity>1:
            cart.quantity-=1
            cart.save()
        else:
            cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')
@login_required
def full_remove(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)

        cart.delete()

    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')
@login_required
def orderform(request):
    total=0
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        u=request.user
        cart=Cart.objects.filter(user=u)
        for i in cart:
            total+=i.quantity*i.products.price
        ac=Account.objects.get(accountno=n)
        if (ac.amount >= total):
            ac.amount=ac.amount-total
            ac.save()
            for i in cart:
                o=Order.objects.create(user=u,products=i.products,address=a,phone=p,order_status="Paid",noofitems=i.quantity)
                i.products.stock=i.products.stock-i.quantity
                i.save()
                o.save()
            cart.delete()
            msg="Ordered Successfully"
            return render(request,"orderdetails.html", {'msg': msg, 'total': total})
        else:
            msg="Insufficient Amount. You can't Place order"
            return render(request,'orderdetails.html',{'msg': msg})
    return render(request, "orderform.html")

@login_required
def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u,order_status="Paid")
    return render(request,'orderview.html',{'o':o,'name':u.username})
