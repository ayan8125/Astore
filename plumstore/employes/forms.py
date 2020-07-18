from django import forms
from .models import employes

class signupphase1(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}))
    lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-Mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Set Password'}))
    phonenumber = forms.IntegerField(   widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

class signupphase2(forms.Form):
    State = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'state'}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'FlatNo/ House np, Building Name'}))
    address12 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street name, Area name'}))
    city = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'city'}))
    zipcode = forms.IntegerField( widget=forms.TextInput(attrs={'placeholder': 'zipcode'}))

class signupphase3(forms.Form):
    Username = forms.CharField()
    password = forms.CharField()
    passwordconfirm = forms.CharField()