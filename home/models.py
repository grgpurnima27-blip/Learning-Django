from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    prize= models.IntegerField(null=True)
    
    def __str__(self):
        return f"title:{self.title}"

