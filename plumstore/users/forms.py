from django import forms
from plumber.models import user

rep = (
    (1,'TV'),
    (2,'Motor'),
    (3,'Washing Machine')
)
class signup(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-Mail'}))
    phonenumber = forms.IntegerField(   widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    phonenumber2 = forms.IntegerField( widget=forms.TextInput(attrs={'placeholder': 'Alternative Number'}))
    State = forms.CharField(   widget=forms.TextInput(attrs={'placeholder': 'Maharastra'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'FlatNo/ House np, Building Name'}))
    address12 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street name, Area name'}))
    city = forms.CharField(   widget=forms.TextInput(attrs={'placeholder': 'city'}))
    zipcode = forms.IntegerField(  widget=forms.TextInput(attrs={'placeholder': 'zipcode'}))
    # zipcode1 = forms.IntegerField(  widget=forms.TextInput(attrs={'placeholder': 'Search'}))

class signupphase1(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-Mail'}))
    phonenumber = forms.IntegerField(   widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

class signupphase2(forms.Form):
    State = forms.CharField(   widget=forms.TextInput(attrs={'placeholder': 'state'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'FlatNo/ House np, Building Name'}))
    address12 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street name, Area name'}))
    city = forms.CharField(   widget=forms.TextInput(attrs={'placeholder': 'city'}))
    zipcode = forms.IntegerField(  widget=forms.TextInput(attrs={'placeholder': 'zipcode'}))

class signupphase3(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Set Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Set Password'}))
    passwordconfirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))



class login(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



class otps(forms.Form):
    otp = forms.CharField(widget=forms.TextInput())

class profile1(forms.ModelForm):
    class Meta:
        model = user
        fields = ['profile','firstname','lastname','email','Phonenumber','Phonenumber2','state','address1','address12','city','zipcode']
    
    

class profile2(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Phonenumber','Phonenumber2','state','address1','address12','city','zipcode']    


class Repairer(forms.Form):
    work = forms.ChoiceField(choices=rep)
   