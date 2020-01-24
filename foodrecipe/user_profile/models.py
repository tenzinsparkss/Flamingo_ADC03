from django.db import models
from main.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age =models.IntegerField()
    description=models.CharField(max_length=200)
    