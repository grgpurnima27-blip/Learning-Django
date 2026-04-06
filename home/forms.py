from django import forms
from .models import Post 
class CreatePost (forms.ModelForm):
    class Meta:  # meta= raw data # gives info about data
        model = Post 
        # fields= "__all__"
        fields = [ 'title','content','prize','photo']

class EditPost(forms.ModelForm):
    class Meta:
        model= Post
        fields= ['title','content']