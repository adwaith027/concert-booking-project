from django import forms
from .models import usermodel,concertmodel,ticketbooking

class userform(forms.ModelForm):
    class Meta:
        model=usermodel
        fields=['username','email','password']
        labels={
            'username':'Username',
            'email':'Email',
            'password':'Password'
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            }
        
class loginform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=200)
    labels={
            'username':'Username',
            'password':'Password',
        }
    widgets={
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'}),
    }


class concertForm(forms.ModelForm):
    class Meta:
        model=concertmodel
        fields='__all__'
        labels={
            'concertname':'Concert Name',
            'concertdate':'Concert Date',
            'concerttime':'Concert Time',
            'concertvenue':'Concert Venue',
            'ticketprice':'Ticket Price',
            'availabletickets':'Available Tickets',
        }

class ticketbookingform(forms.ModelForm):
    class Meta:
        model=ticketbooking
        fields='__all__'
