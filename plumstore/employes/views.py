from django.shortcuts import render,redirect
from .forms import signupphase3
import re
from .models import employes
"""  Regular Expression for validation"""

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


""" Login Form """
def mastersignup(request):
    check_state = {}
    if request.method == 'POST':
        form = signupphase3(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Username']
            code = form.cleaned_data['password']
            code1 = form.cleaned_data['passwordconfirm']
            print(name,code,code1)
            match1 = re.search(userpattern,name)
            user2 = employes.objects.filter(username=name)
            check_state['form']=form
            if len(user2)!=0:
                check_state['user_exist'] = 1
            if match1 == None:
                check_state['invalid_user'] = 1
            if (code1 == code)==False:
                check_state['passnot'] = 1
            if (match1 != None) and ((code1 == code)==True) and (len(user2) == 0):
                user1=employes(username=name,password=code)
                # user.objects.filter(username='username').delete()
                response =  redirect('plum-home')
                response.set_cookie('username',name)
                return response
            else:
                return render(request, 'employes/signup1.html', check_state) 
            
    else:
        form = signupphase3()
    return render(request, 'employes/signup1.html', {'form':form}) 