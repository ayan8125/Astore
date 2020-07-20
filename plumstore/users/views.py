from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from users.forms import signup,signupphase1,signupphase2,signupphase3,login,otps,profile2
from django.contrib import messages
from django import forms
from plumber.models import user
from twilio.rest import Client
import random
from plumber.models import user
from orders.models import orders
import re
from itsdangerous import TimedJSONWebSignatureSerializer as serializer
import smtplib
from django.contrib.sessions.backends.db import SessionStore

# from plumstore import settings
account_Sid = '*******'
auth_token = '*****'
email_add = 'ayanshaikh7187@gmail.com'
def generate_otp():
    strs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    otp = ''
    for i in range(6):
        otp += strs[ random.randint(0,(len(strs)-1))]
    return otp

def sendsms(tonumber,otp):
    message = f'Your One Time Password(OTP) is {otp}.Dont Share this with anyone and is only valid for some time' 
    client = Client(account_Sid,auth_token)
    client.messages.create(to = ('+91' + str(tonumber)),from_='+19384448948',body=message)
    






pattern = re.compile(r'[a-zA-Z]')
# email_pattern = re.compile(r'[a-zA-Z0-9]+@[a-z]+\.[a-zA-z]{1,5}')    
email_pattern = re.compile(r'^([_\-\.a-zA-Z0-9]+)@([_\-\.a-zA-Z]+)\.([a-zA-Z]){2,7}$')
phone = re.compile(r'[0-9]{10}')
address_pattern = re.compile(r'[a-zA-Z0-9,-]')
citypattern = re.compile(r'[a-zA-Z]+')
statepattern = re.compile(r'[a-zA-Z]+')
zipcodepattern = re.compile(r'[0-9]')
userpattern = re.compile(r'[a-zA-Z0-9]{2,10}')
# Create your views here.
#

SECRET_KEY = '******'


def base(request):
    return render(request, 'users/test.html')


def test(request):
    pass

def give_token(usernames):
    s = serializer(SECRET_KEY,180)
    token = s.dumps({'username1':usernames}).decode('utf-8')
    return token



def sendemail(usernames, email):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        links = 'http://localhost:8000/email_confirm/'
        link = give_token(usernames)
        smtp.login(email_add,'********')
        subject = 'Click on the below link for further processs'
        body = f'{links + link}'
        msg = f'Subject: {subject}\n\nClink on the Give Link , which will take you to your last stage of registration\n\n{body}\n\n\nif you did not made this reuest than simply ignore it'
        smtp.sendmail(email_add,email,msg)





def validate_token(token):
    s = serializer(SECRET_KEY)
    try:
        username = s.loads(token)['username1']
    except:
        return None
    return username


def email_confirm(request,token):
    # token = give_token('ayan8125')
    # print(token)
    res = validate_token(token)
    if res != None:
        print(res)
        return redirect('signup2')
    else:
        return redirect('plum-home')

@login_required(login_url='signup3')
def signup1(request):
    check  = []
    check_state = {}
    name_stat = 1
    last_stat = 1
    email_stat = 1            
    num_stat = 1
    if request.method == 'POST':
        form = signupphase1(data = request.POST)
        print('here.........................................')
        print(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            matchname = re.search(pattern,firstname)
            if(matchname != None):
                print("vALID nAME")
            else:
                name_stat = 0
            lastname = form.cleaned_data['lastname']
            matchlast = re.search(pattern,lastname)
            if(matchlast != None):
                print("vALID nAME")
            else:
                last_stat = 0
            email = form.cleaned_data['email']
            print(email)
            matchemail = re.search(email_pattern,email)
            if(matchemail != None):
                print("vALID email")
            else:
                email_stat = 0
                print("Invalid Email")
            Pnumber = form.cleaned_data['phonenumber']
            print(Pnumber)
            matchnum = re.search(phone,str(Pnumber))
            if(matchnum != None):
                print("vALID Number")
            else:
                num_stat = 0
                print("Invalid Number")
            if(name_stat==0):
                check.append('name_stat')
            if(last_stat==0):
                check.append('last_state')
            if(email_stat==0):
                check.append('email_stat')
            if(num_stat==0):
                check.append('Pnumber')

            check_state['form'] = form
            for i in check:
                check_state[i] = 1 
            print(check)
            print(check_state)             
            if name_stat and last_stat and email_stat and num_stat:
                temp = request.POST['firstname']
                user1=user(firstname=firstname,lastname=lastname,email=email,Phonenumber=Pnumber)
                user1 = user.objects.filter(username=request.COOKIES['username']).first()
                user1.firstname = firstname
                user1.lastname = lastname
                user1.email = email
                user1.Phonenumber = Pnumber
                user1.save()
                return redirect('auth')
            else:
                print(check)
                print(check_state) 
                return render(request, 'users/signup1.html', check_state) 

        
    else:
        form = signupphase1()
    return render(request, 'users/signup1.html', {'form':form})    

@login_required(login_url='signup1')
def signup2(request):
    check  = []
    check_state = {}
    address_stat = 1
    address2_stat = 1
    zip_stat = 1
    state_stat = 1
    city_stat = 1
    if request.method == 'POST':
        form = signupphase2(data = request.POST)
        if form.is_valid():

            State = form.cleaned_data['State']
            matchstate = re.search(statepattern,State)
            if(matchstate != None):
                print("vALID State")
            else:
                state_stat = 0
                print(state_stat)
                print("Invalid state")
            address1 = form.cleaned_data['address1']
            matchaddres = re.search(address_pattern,address1)
            if(matchaddres != None):
                print("vALID addresss")
            else:
                address_stat = 0
                print("Invalid addreess")
                print(address2_stat)
            address2 = form.cleaned_data['address12']
            matchaddres2 = re.search(citypattern,address2)
            if(matchaddres2 != None):
                print("vALID addresss")
            else:
                address2_stat = 0
                print("Invalid addreess")
            city = form.cleaned_data['city']
            matchcity= re.search(citypattern,city)
            if(matchcity != None):
                print("vALID city")
            else:
                city_stat = 0
                print("Invalid city")
            zipcode = form.cleaned_data['zipcode']
            print(zipcode)
            matchzipcode= re.search(zipcodepattern,str(zipcode))
            if(type(zipcode) == int):
                print("vALID code")
            else:
                zip_stat = 0
                print("Invalid code")            
            if(state_stat==0):
                check.append('state_stat')
            if(address2_stat==0):
                check.append('address2_stat')
            if(address_stat==0):
                check.append('address_stat')
            if(city_stat==0):
                check.append('city_stat')
            if(zip_stat==0):
                check.append('zip_stat')
            check_state['form'] = form
            for i in check:
                check_state[i] = 1
            print(check)
            print(check_state)
            if state_stat  and address_stat  and address2_stat  and city_stat and zip_stat:
                user1 = user.objects.filter(username=request.COOKIES['username']).first()
                firstnames = user1.firstname
                user_name = user1.username
                user1.state = State
                user1.city = city
                user1.address1 = address1
                user1.address12 = address2
                user1.zipcode = zipcode
                user1.save()
                messages.success(request, f'hey { firstnames }! Your Account Was Created Suucessfully with Username { user_name } , Please Login with Your Username and Password.')
                return redirect('login')
            else:
                return render(request, 'users/signup2.html', check_state)
    else:
        form = signupphase2()
    return render(request, 'users/signup2.html', {'form':form}) 

def signup3(request):
    check_state = {}
    if request.method == 'POST':
        form = signupphase3(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Username']
            code = form.cleaned_data['password']
            code1 = form.cleaned_data['passwordconfirm']
            print(name,code,code1)
            match1 = re.search(userpattern,name)
            user2 = user.objects.filter(username=name)
            check_state['form']=form
            if len(user2)!=0:
                check_state['user_exist'] = 1
            if match1 == None:
                check_state['invalid_user'] = 1
            if (code1 == code)==False:
                check_state['passnot'] = 1
            if (match1 != None) and ((code1 == code)==True) and (len(user2) == 0):
                user1=user(username=name,password=code)
                user1.username = name
                user1.password = code
                user1.save()
                # user.objects.filter(username='username').delete()
                response =  redirect('signup1')
                response.set_cookie('username',name)
                return response
            else:
                return render(request, 'users/signup3.html', check_state) 
            
    else:
        form = signupphase3()
    return render(request, 'users/signup3.html', {'form':form}) 



from django.http import HttpResponse

# @login_required(login_url='login')
def log(request):
    check_state = {}
    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Username']
            code = form.cleaned_data['password']
            print(name,code)
            user2 = user.objects.filter(username=name)
            check_state['form']=form
            user3 = user.objects.filter(username=name).first()
            if (len(user2) != 0) and ((user3.password == code)==False):
                check_state['wrongpass'] = 1
            if (len(user2) == 0):
                check_state['notexist'] = 1
            print(check_state)
            if len(user2) != 0:
                if ((user3.password == code)==True):
                    strs = '/'+str(name)
                    response =  redirect(strs)
                    response.set_cookie('username',name)
                    return response
            else:
                print("ehatus -----------------------------------")
                return render(request, 'users/login.html', check_state) 
    else:
        form = login()
    request.session.set_test_cookie()
    return render(request, 'users/login.html', {'form':form}) 





# @login_required(login_url='signup2')
def auth(request):
    check_state = {}
    otp = ""
    
    if request.method == 'POST':
        form = otps(request.POST)
        print(request.POST['otp'],otp)
        if request.POST['otp'] == request.COOKIES['otp']:
            check_state['success'] = 1
            sendemail('ayan8125','ayanshaikh1522@gmail.com')
            return render(request, 'users/otp.html', check_state)
        else:
            check_state['form'] = form
            check_state['nootp'] = 1
            return render(request, 'users/otp.html', check_state)

    form = otps()
    otp = generate_otp()
    sendsms(9359710334,otp)
    response =  render(request, 'users/otp.html',{'form':form})
    response.set_cookie('otp',otp)
    return response



def logout(request):
    response =  redirect('plum-home')
    response.delete_cookie('username')
    return response
