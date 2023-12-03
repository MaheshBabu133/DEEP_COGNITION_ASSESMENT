from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class employee_data(models.Model):
    identity = models.CharField(primary_key = True, max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique = True,null = False, max_length=254)
    mno = models.IntegerField()
    dob = models.DateField()
    age = models.IntegerField()
    profile_pic = models.ImageField(upload_to='pp')
    address = models.TextField()
    Biodata = models.TextField(default = 'Nothing to say')


    def __str__(self):
        return self.identity
