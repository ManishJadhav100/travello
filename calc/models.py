from django.db import models


# Create your models here.
class Destination(models.Model):

     name = models.CharField(max_length=100)
     img = models.ImageField(upload_to='pics')
     desc = models.TextField()
     price = models.IntegerField()
     offer = models.BooleanField(default=False)


class News_post(models.Model):

     objects = None
     img = models.ImageField(upload_to='pics')
     desc = models.TextField()
     date = models.IntegerField()
     month = models.TextField(max_length=10)
