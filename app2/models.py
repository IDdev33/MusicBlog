from django.db import models
from datetime import datetime

# Create your models here.


class Subscriber(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)

class Article(models.Model):
    Image = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=50)
    Added_at = models.DateTimeField(default=datetime.now, blank=True)
    Link = models.CharField(max_length=100)
    Text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    

class Track(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='tracks')
    link = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
