from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

class SigninForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "Username",  "style" : "border: 1px solid #d3d5d8 !important;"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

