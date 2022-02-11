from django.urls import path
from . import views






urlpatterns = [
   
    path('',views.StudentApi.as_view()),
    path('/<int:pk>',views.StudentApi1.as_view()),
    path('home',views.home),
]