from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)



class Product(models.Model):
    pname = models.CharField(max_length=100)
    pnumber = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.pname

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created = False,**kwargs):
    if created:
            token = Token.objects.create(user=instance)
            print("Generated token :  " , token)
