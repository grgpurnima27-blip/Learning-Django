from django import forms 
from django.contrib.auth.models import User
from .models import CustomUser
class UserCreationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=['username','email','password','confirm_password','phone','Last_name','First_name']

        def clean(self): # from validation
            cleaned_data= super().clean()
            password=cleaned_data.get("password")
            confirm_password= cleaned_data.get('confirm password')

            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")
            
        def save(self, commit=True):  # data save 
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user

class UserLoginForm(forms.Form):  #login form
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)