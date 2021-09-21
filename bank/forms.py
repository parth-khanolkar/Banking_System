from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class ActionForm(forms.ModelForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    email_id =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    contact =  forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True'}))
    class Meta:
        model = Deposit
        fields = ["username", "email_id", "contact", "amount"]

class TransactionForm(forms.ModelForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    email_id =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    contact =  forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'True'}))
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), initial=0)
    class Meta:
        model = Transact
        fields = ["username", "email_id", "contact", "amount","receiver"]