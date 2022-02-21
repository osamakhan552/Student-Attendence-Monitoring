from rest_framework import serializers
from api.models import  User,student,teacher






class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('email','first_name', 'last_name','phone','username','roleId','address','password')


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('age','roll','state','userId','birth_date','div')




class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = ('age','state','userId','birth_date','qualification')