from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer,studentSerializer,teacherSerializer
from .models import student,User,teacher
from django.core import *


# Create your views here.
def home(request):

    return HttpResponse("Working!!!!!")



class UserAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentDetialAPI(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

class TeacherDetialAPI(generics.ListCreateAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer
