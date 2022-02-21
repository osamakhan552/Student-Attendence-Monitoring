from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE, SET_NULL
from rest_framework.authtoken.models import Token
import uuid
from django.core.validators import MinLengthValidator
from datetime import date,datetime,timedelta


  

class roles(models.Model):
    roleId =  models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False,unique=True)
    roleName = models.CharField(max_length=10)
    def __str__(self):
        return self.roleName



class User(AbstractUser):

    email = models.EmailField(_('email address'))
    ID =  models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10,default="0000000000",validators=[MinLengthValidator(10)])
    roleId = models.ForeignKey(roles,CASCADE,related_name="roles" ,null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username


class student(models.Model):
    userId = models.OneToOneField(User,on_delete=CASCADE)
    age =   models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    birth_date = models.DateField(default=datetime.now)
    div = models.CharField(max_length=5,null=True)
    roll =  models.CharField(max_length=100,null=True)
   
    
    def __str__(self):
        return self.userId.first_name



class teacher(models.Model):
    userId = models.OneToOneField(User,on_delete=CASCADE)
    qualification = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    birth_date = models.DateField(default=datetime.now)
    age =   models.CharField(max_length=100,null=True)

   

    def __str__(self):
        return self.userId.first_name

standard_choice =(
    ("1", "1st"),
    ("2", "2nd"),
    ("3", "3rd"),
    ("4", "4th"),
    ("5", "5th"),
    ("6", "6th"),
    ("7", "7th"),
    ("8", "8th"),
    ("9", "9th"),
    ("10", "10th"),
)

class batch(models.Model):
    year = models.CharField(max_length=20,null=True)
    std = models.CharField(
        max_length = 20,
        choices = standard_choice,
        default = '1'
        )
    teacher = models.ForeignKey(teacher,on_delete=CASCADE)
    class Meta:
        unique_together = ('year', 'std')



class attendance(models.Model):
    attendDate = models.DateField(default=datetime.now)
    status = models.BooleanField(default=True)
    batch = models.ForeignKey(batch,on_delete=CASCADE)


class attendanceMapping(models.Model):
    student = models.ForeignKey(student,on_delete=CASCADE)
    attendance = models.ForeignKey(attendance,on_delete=CASCADE)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created = False,**kwargs):
    if created:
            token = Token.objects.create(user=instance)
            print("Generated token :  " , token)
            # print('Creating job')
            # arg1 = instance.username
            # arg2 = 'Khan'
            # start(arg1,arg2,str(token))
            