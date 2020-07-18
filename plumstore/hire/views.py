from django.shortcuts import render,redirect
from plumber.models import user
from hire.models import hire
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def hire_plumber(request,usernames):
    try:
        obj = user.objects.filter(username=usernames).first()
        address = f'{obj.address1} {obj.address12} {obj.city} {obj.zipcode} {obj.state}'
        mobile = obj.Phonenumber
        alternate= obj.Phonenumber2
        if obj != None and usernames != request.COOKIES['username']:
            return render(request,'users/authentication.html',{'status':1})
        return render(request, 'hire/plumber.html',{'username':request.COOKIES['username'],'product':request.COOKIES['product'],'address':address,'mobile':mobile,'alternate':alternate})
    except:
        return render(request,'users/authentication.html',{'status1':1})
def  hire_repairer(request,usernames):
    try:
        obj = user.objects.filter(username=usernames).first()
        address = f'{obj.address1} {obj.address12} {obj.city} {obj.zipcode} {obj.state}'
        mobile = obj.Phonenumber
        alternate= obj.Phonenumber2
        if obj != None and usernames != request.COOKIES['username']:
            return render(request,'users/authentication.html',{'status':1})
        return render(request, 'hire/repairer.html',{'username':request.COOKIES['username'],'product':request.COOKIES['product'],'address':address,'mobile':mobile,'alternate':alternate,'tv':1,'motor':1,'wash':1})
    except:
        return render(request,'users/authentication.html',{'status1':1})

def hire_electricians(request,usernames):
    try:
        obj = user.objects.filter(username=usernames).first()
        address = f'{obj.address1} {obj.address12} {obj.city} {obj.zipcode} {obj.state}'
        mobile = obj.Phonenumber
        alternate= obj.Phonenumber2
        if obj != None and usernames != request.COOKIES['username']:
            return render(request,'users/authentication.html',{'status':1})
        return render(request, 'hire/electricians.html',{'username':request.COOKIES['username'],'product':request.COOKIES['product'],'address':address,'mobile':mobile,'alternate':alternate})
    except:
        return render(request,'users/authentication.html',{'status1':1})
        
# @login_required(login_url='login')
def hires1(request, usernames):
    try:
        hires = hire.objects.filter(user_id= usernames).order_by('-hire_date')
        users = user.objects.filter(username=usernames).first()
        try:
            if(usernames != request.COOKIES['username'] and users != None):
                return render(request, 'users/authentication.html',{'status':1})
            if(usernames != request.COOKIES['username'] and users == None):
                return render(request,'users/authentication.html',{'status1':1})
        except:
            return render(request, 'users/authentication.html',{'status':1}) 
        print(hires)
        if hires != None: 
            context = {'username': usernames,'hires':hires}  
            return render(request, 'hire/hire.html', context)
        else:
            return render(request, 'hire/hire.html')
    except:
        return render(request, 'users/authentication.html',{'status1':1})   




def user_hire(request,usernames):
    name = request.COOKIES['username']
    product = request.COOKIES['product']
    hire.objects.create(hire_product=product, hire_status = 1,hire_type=1,user_id=name)
    messages.success(request, f'Your Hiring Process has been confirm, our employee will be reaching but before that you will get call from us for helping you more.')
    strs = '/'+ str(name)
    return redirect(strs)

def plumber_hire(request,usernames):
    name = request.COOKIES['username']
    hire.objects.create(hire_product="Plumber", hire_status = 1,hire_type=1,user_id=name)
    messages.success(request, f'Your Hiring Process has been confirm, our employee will be reaching but before that you will get call from us for helping you more.')
    strs = '/'+ str(name)
    return redirect(strs) 

def electricians_hire(request,usernames):
    name = request.COOKIES['username']
    hire.objects.create(hire_product="Electricians", hire_status = 1,hire_type=1,user_id=name)
    messages.success(request, f'Your Hiring Process has been confirm, our employee will be reaching but before that you will get call from us for helping you more.')
    strs = '/'+ str(name)
    return redirect(strs)  