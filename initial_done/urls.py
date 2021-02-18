
from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginset,name='index'),
    path('register/',views.register,name='register'),
    path('get/',views.get.as_view()),
    path('post/',views.get.as_view()),
    
    
    
    
]
