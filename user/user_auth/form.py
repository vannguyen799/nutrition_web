from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=5, required=True)
    firstname = forms.CharField(min_length=3, max_length=30, required=True)
    lastname = forms.CharField(min_length=3, required=True, max_length=30)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    agree_terms = forms.BooleanField(required=True)
