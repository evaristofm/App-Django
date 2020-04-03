from django import forms

class RegistroForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email =forms.EmailField(max_length=100)
    phone =forms.CharField(max_length=50)
