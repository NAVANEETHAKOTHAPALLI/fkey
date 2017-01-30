

from django.db import models
from PIL import Image
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import datetime

# Create your models here.
class Comment(models.Model):
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    highlighted = models.TextField()
    
    class Meta:
        ordering = ['timestamp']    



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=r'/home/navaneetha/Pictures', null=True, blank=True)
    published = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200)
    subscibers = models.IntegerField(default=0)
    subscribe = models.EmailField()
    draft = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    highlighted = models.TextField()
    comment = models.ForeignKey(Comment, related_name='comments', on_delete=models.CASCADE)

    class Meta:
    	ordering = ['published','updated_date']

