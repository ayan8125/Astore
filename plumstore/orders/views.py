from django.shortcuts import render
from orders.models import orders
from django.db.models import Sum
from plumber.models import user

from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url='login')
def order1(request, usernames):
    # try:
    order = orders.objects.filter(user_id= usernames , status=0).order_by('-order_date')
    users = user.objects.filter(username=usernames).first()
    try:
        if(usernames != request.COOKIES['username'] and users != None):
            return render(request, 'users/authentication.html',{'status':1})
        if(usernames == request.COOKIES['username'] and users == None):
            return render(request,'users/authentication.html',{'status1':1})
        if(order == None and usernames == request.COOKIES['username']):
            print(type(order))
            return render(request, 'orders/orders.html',{'status1':1,'username':order1.username})
    except:
        return render(request, 'users/authentication.html',{'status':1})

    try:
        total = orders.objects.filter(user_id= usernames , status=0).aggregate(Sum('cost'))
        discounts = orders.objects.filter(user_id= usernames , status=0).order_by('-order_date').first().discount
        total_amount = total['cost__sum'] - total['cost__sum'] * ((discounts)/100)
        discount_amount = total['cost__sum'] * ((discounts)/100)
        if order != None: 
            context = {'username': usernames,'order':order,'total_amount':total_amount,'discounts':discounts,'total':total['cost__sum'],'discount_amount':discount_amount}
            return render(request, 'orders/orders.html', context)
    except:
        return render(request,'orders/orders.html',{'status1':1,'username':usernames})  
        
    # except:
    #     order = orders.objects.filter(user_id= usernames , status=0).order_by('-order_date')
    #     order1 = user.objects.filter(username= usernames).first()
    #     if order is None and order1 != None:
    #         return render(request, 'orders/orders.html') 
    #     else:
    #         return render(request, 'users/authentication.html',{'status1':1}) 
