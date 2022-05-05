from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Comments, Order


class CreateUserForm (UserCreationForm): #Inharits the user creation from django 
    firstname = forms.CharField(max_length=32, label='First name')
    lastname= forms.CharField(max_length=32, label='Last name')
    address= forms.CharField(max_length=32, label='Address')
    phonenumber= forms.CharField(max_length=32, label='Phone Number', )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'firstname', 'lastname', 'address', 'phonenumber']


class CreateCommentForm(ModelForm):


    class Meta:
        model = Comments
        fields = ('ISBN', 'Username', 'Comment')

class CreateOrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'