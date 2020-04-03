from django import forms

class RegistroForm(forms.Form):
    user_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite usuário'}))

    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite senha'}))

    email =forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite email'}))

    phone =forms.CharField(max_length=50, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite telefone'}))
