from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from plumber.models import user 
from orders.models import orders
from django.contrib.auth import logout
from users.forms import profile1,profile2
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
import re
from users.forms import Repairer
from hire.models import hire
import datetime


pattern = re.compile(r'[a-zA-Z]')
email_pattern = re.compile(r'[a-zA-Z0-9]+@[a-z]+\.[a-zA-z]{1,5}')    
# email_pattern = re.compile(r'^([_\-\.a-zA-Z0-9]+)@([_\-\.a-zA-Z]+)\.([a-zA-Z]){2,7}$')
phone = re.compile(r'[0-9]{10}')
address_pattern = re.compile(r'[a-zA-Z0-9,-]')
citypattern = re.compile(r'[a-zA-Z]+')
statepattern = re.compile(r'[a-zA-Z]+')
zipcodepattern = re.compile(r'[0-9]')
userpattern = re.compile(r'[a-zA-Z0-9]{2,10}')
# Create your views here.

def home(request):
    return render(request, 'plumber/home.html')

def about(request):
    return HttpResponse('<h1>Plumber | About</h1>')


# @login_required(login_url='login')
def profile(request,usernames):
    modes = {}
    email_state=1
    number_state=1
    name_state=1
    last_state= 1
    city_state=1
    zip_state=1
    number2_state=1
    try:   
        obj = user.objects.filter(username = usernames).first()
        try:
            if(obj != None and usernames != request.COOKIES['username']):
                return render(request, 'users/authentication.html',{'status':1})
        except:
            return render(request, 'users/authentication.html',{'status':1})
        if obj == None:
            return render(request, 'users/authentication.html',{'status1':1})
        if request.method == 'POST':
            form = profile1(request.POST, request.FILES,instance=obj)
        
            form.fields["firstname"].initial = obj.firstname
            form.fields["lastname"].initial = obj.lastname
            form.fields["email"].initial = obj.email
            form.fields["Phonenumber"].initial = obj.Phonenumber
            form.fields["Phonenumber2"].initial = obj.Phonenumber2
            form.fields["state"].initial = obj.state
            form.fields["address1"].initial = obj.address1
            form.fields["address12"].initial = obj.address12
            form.fields["city"].initial = obj.city
            form.fields["zipcode"].initial = obj.zipcode

            name = re.search(citypattern,request.POST['firstname'])
            last = re.search(citypattern,request.POST['lastname'])
            emails = re.search(email_pattern,request.POST['email'])
            phones = re.search(phone,request.POST['Phonenumber'])
            phones1 = re.search(phone,request.POST['Phonenumber2'])
            zips = re.search(zipcodepattern,request.POST['zipcode'])
            city = re.search(citypattern,request.POST['city'])
            if name == None:
                name_state = 0
                modes['firstname1'] = 1
            if last == None:
                last_state = 0
                modes['lastname1'] = 1
            if emails == None:
                email_state = 0
                modes['email1'] = 1
            if phones == None or (len(str(request.POST['Phonenumber'])) != 10):
                number_state = 0
                modes['pnumber1'] = 1
            if phones1 == None or (len(str(request.POST['Phonenumber2'])) != 10):
                number2_state = 0
                modes['pnumber2'] = 1
            if zips == None:
                zip_state = 0
                modes['zipcode1'] = 1
            if city == None:
                city_state = 0
                modes['city1'] = 1
            print(number_state,number2_state)
            if name_state and last_state and email_state and number_state and zip_state and number2_state: 
                obj = form.save(commit=False)
                obj.save()
                print("IT Has upadted")
                return redirect('/'+str(usernames)+'/profile')
                # return render(request, 'users/profile.html',{'username':obj.username,
                # 'firstname':obj.firstname,
                # 'lastname':obj.lastname,
                # 'pnumber':obj.Phonenumber,
                # 'email':obj.email,
                # 'state':obj.state,
                # 'address1':obj.address1,
                # 'address12':obj.address12,
                # 'city':obj.city,
                # 'zipcode':obj.zipcode,
                # 'profile':obj.profile.url,
                # 'status':1,'form':form
                # })
            else:
                modes['profile'] = obj.profile.url
                modes['form'] = form
                modes['username'] = obj.username
                return render(request, 'users/profile.html',modes)

        else:
            form = profile1()
            form.fields["firstname"].initial = obj.firstname
            form.fields["lastname"].initial = obj.lastname
            form.fields["email"].initial = obj.email
            form.fields["Phonenumber"].initial = obj.Phonenumber
            form.fields["Phonenumber2"].initial = obj.Phonenumber2
            form.fields["state"].initial = obj.state
            form.fields["address1"].initial = obj.address1
            form.fields["address12"].initial = obj.address12
            form.fields["city"].initial = obj.city
            form.fields["zipcode"].initial = obj.zipcode
        model = {
            'username':obj.username,
            'firstname':obj.firstname,
            'lastname':obj.lastname,
            'pnumber':obj.Phonenumber,
            'email':obj.email,
            'state':obj.state,
            'address1':obj.address1,
            'address12':obj.address12,
            'city':obj.city,
            'zipcode':obj.zipcode,
            'profile':obj.profile.url,
            'status':1,
            'form' : form
        }
        return render(request, 'users/profile.html',model)
    except:
        return render(request, 'users/authentication.html',{'status1':1})

def not_auth(request):
    pass






# @login_required(login_url='login')
def valid_user(request,usernames):
    if usernames != request.COOKIES['username']:
        return render(request, 'users/authentication.html',{'status':1})
    if request.method == 'POST':
        form = Repairer(request.POST)
        if form.is_valid():
            print(request.POST)
            obj1 = {}
            strs = '/'+str(usernames)+'/hire-repairer'
            try:
                obj = user.objects.filter(username=usernames).first()
                address = f'{obj.address1} {obj.address12} {obj.city} {obj.zipcode} {obj.state}'
                mobile = obj.Phonenumber
                alternate= obj.Phonenumber2
                try:
                    if obj is not None and usernames != request.COOKIES['username']:
                        return render(request, 'users/authentication.html',{'status':1})
                except:
                    return render(request, 'users/authentication.html',{'status':1})  
                if request.POST['work']=='1':
                    cook="Television Screen"
                    hire.objects.create(hire_product='Television Screen',hire_status=1,hire_type=1,hire_date=datetime.datetime.now(),user_id=usernames)
                    response =  render(request , 'hire/repairer.html',{'username': usernames,'tv':1,'address':address,'mobile':mobile,'alternate':alternate,})
                    response.set_cookie('product',cook)
                    return response
                if request.POST['work']=='3':
                    cook = "Washing Machine"
                    hire.objects.create(hire_product='Wahing Machine',hire_status=1,hire_type=1,hire_date=datetime.datetime.now(),user_id=usernames)
                    response =  render(request , 'hire/repairer.html',{'username': usernames,'wash':1,'address':address,'mobile':mobile,'alternate':alternate,})
                    response.set_cookie('product',cook)
                    return response
                if request.POST['work']=='2':
                    cook = "motor"
                    hire.objects.create(hire_product='Motor',hire_status=1,hire_type=1,hire_date=datetime.datetime.now(),user_id=usernames)
                    response =  render(request , 'hire/repairer.html',{'username': usernames,'motor':1,'address':address,'mobile':mobile,'alternate':alternate,})
                    response.set_cookie('product',cook)
                    return response
                print('username', usernames)
                obj = user.objects.filter(username = usernames).first()
                if obj != None:
                    obj1['username'] = usernames
                    return render(request , 'users/user.html',{'username': usernames, 'form':form})
            except:
                return render(request, 'users/authentication.html',{'status1':1})
                   
                
    else:
        form = Repairer()
        return render(request, 'users/user.html',{'username':usernames,'form':form})
        



# login_required(login_url='login')
def editProfile(request,usernames):
    modes = {}
    email_state=1
    number_state=1
    name_state=1
    last_state= 1
    city_state=1
    zip_state=1
    number2_state=1  
    try: 
        obj = user.objects.filter(username = usernames).first()
        if obj is not None and usernames != request.COOKIES['username']:
            return render(request, 'users/authentication.html',{'status':1})
        if request.method == 'POST':
            form = profile2(request.POST, request.FILES,instance=obj)
            form.fields["Phonenumber"].initial = obj.Phonenumber
            form.fields["Phonenumber2"].initial = obj.Phonenumber2
            form.fields["state"].initial = obj.state
            form.fields["address1"].initial = obj.address1
            form.fields["address12"].initial = obj.address12
            form.fields["city"].initial = obj.city
            form.fields["zipcode"].initial = obj.zipcode
            phones = re.search(phone,request.POST['Phonenumber'])
            phones1 = re.search(phone,request.POST['Phonenumber2'])
            zips = re.search(zipcodepattern,request.POST['zipcode'])
            city = re.search(citypattern,request.POST['city'])
            if phones == None or (len(str(request.POST['Phonenumber'])) != 10):
                number_state = 0
                modes['pnumber1'] = 1
            if phones1 == None or (len(str(request.POST['Phonenumber2'])) != 10):
                number2_state = 0
                modes['pnumber2'] = 1
            if zips == None:
                zip_state = 0
                modes['zipcode1'] = 1
            if city == None:
                city_state = 0
                modes['city1'] = 1
            print(number_state,number2_state)
            if  number_state and zip_state and number2_state: 
                obj = form.save(commit=False)
                obj.save()
                print("IT Has upadted")
                return redirect('/'+str(usernames)+'/profile')
    
            else:
                modes['forms'] = form
                modes['username'] = obj.username
                modes['form'] = form
                return render(request, 'users/editprofile.html',modes)

        else:
            form = profile2()
            form.fields["Phonenumber"].initial = obj.Phonenumber
            form.fields["Phonenumber2"].initial = obj.Phonenumber2
            form.fields["state"].initial = obj.state
            form.fields["address1"].initial = obj.address1
            form.fields["address12"].initial = obj.address12
            form.fields["city"].initial = obj.city
            form.fields["zipcode"].initial = obj.zipcode
        model = {
            'pnumber':obj.Phonenumber,
            'state':obj.state,
            'address1':obj.address1,
            'address12':obj.address12,
            'city':obj.city,
            'zipcode':obj.zipcode,
            'profile':obj.profile.url,
            'status':1,
            'form' : form
        }   
        return render(request,'users/editprofile.html',{'forms':form,'username':usernames})
    except:
        return render(request, 'users/authentication.html',{'status1':1})







