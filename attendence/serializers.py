from rest_framework import serializers
from .models import Student,Product


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
    

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'pname', 'pnumber', 'price']
        read_only_feilds = ['pname']