from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Student,Product
from .serializers import StudentSerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



# Create your views here.
def home(request):

    return HttpResponse("Working!!!!!")


class StudentApi(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Student.objects.all()
    def get_serializer_class(self):
        print('osama get')
        print(self.request.user)
        return StudentSerializer
   

       

class StudentApi1(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

