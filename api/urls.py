from django.urls import path
from . import views






urlpatterns = [
   
    path('',views.home),
    path('user',views.UserAPI.as_view()),
    path('user/student',views.StudentDetialAPI.as_view()),
    path('user/teacher',views.TeacherDetialAPI.as_view()),
]