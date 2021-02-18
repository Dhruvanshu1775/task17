from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from rest_framework import generics

from .models import Admin_part, User_part
from .serializers import userserializer

# Create your views here.


class get(generics.ListAPIView):
    queryset = User_part.objects.all()
    serializer_class = userserializer

class post(generics.ListCreateAPIView):
    queryset = User_part.objects.all()
    serializer_class = userserializer



def loginset(request):
    if request.method == 'POST':
        if User_part.objects.filter(email=request.POST['email'], password1=request.POST['password1']).exists():
            user1 = User_part.objects.get(email=request.POST['email'], password1=request.POST['password1'])
            return render(request, 'customer.html', {'user1': user1})
        elif Admin_part.objects.filter(email=request.POST['email'], password1=request.POST['password1']).exists():
            user2 = Admin_part.objects.get(email=request.POST['email'], password1=request.POST['password1'])
            obj1 = User_part.objects.all()
            return render(request,'admin_dash.html', {'user2': user2,'obj1':obj1})    

        else:
            messages.info(request, 'INVALID DATA')
            return redirect('/')
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        status_choices = request.POST['status_choices']
        

        if password1 == password2:
            if User_part.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                created = User_part(first_name=first_name, last_name=last_name,email=email, password1=password1, password2=password2,status_choices = status_choices)
                created.save()
                print('user done')
            return redirect('/')
        else:
            messages.info(request, 'password did not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
