from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    prize= models.IntegerField(null=True)
    photo= models.ImageField(upload_to='photos',null=True)

    
    def __str__(self):
        return f"title:{self.title}"

