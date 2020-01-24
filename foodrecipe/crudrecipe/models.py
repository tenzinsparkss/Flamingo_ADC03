from django.db import models


# Create your models here.
class Cookbook(models.Model):

    title= models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    pdf = models.FileField(upload_to = "media/pdfs")
