from django.shortcuts import render

# Create your views here.

from django.contrib.auth  import get_user_model

User = get_user_model()


from django.shortcuts import render ,HttpResponse,redirect

from django.contrib import messages

# Create your views here.
import uuid

from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout
from django.core.mail import send_mail,EmailMessage
from datetime import datetime, timedelta
import csv

from .models import *

def RegisterUser(request,):
    form  = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            # email = request.POST.get('email')

            user = form.save()
            password = user.password
            user.set_password(password)
            user.save()

            return render(request,'login.html')
           
        else:
            form  = UserRegisterForm(request.POST)
            return render(request,'register.html',locals())
        
    return render(request,'register.html')


def Login(request):
    if  request.method == "POST":
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request, user)
            user=request.user
            # return HttpResponse("Login Succfully")
            return render(request,'dash_board.html')
            
        
        else:
            messages.info(request ,"Incorrect Username or Password")
            return HttpResponse("Not login")
    return render(request,'login.html')


def logout(request):
    user_logout(request)
    return redirect('/login')

import csv

import csv
import io

def dash(request):
    if request.method == "POST":
        uploaded_file = request.FILES['uploadInput']
        file_data = uploaded_file.read().decode('utf-8')
        file_stream = io.StringIO(file_data)  # Create a file stream in text mode
        csv_reader = csv.reader(file_stream)
        header_row = next(csv_reader)

        for row in csv_reader:
            if len(row) >= 2:  # Check if row has at least 2 elements
                column1 = row[0]
                column2 = row[1]
                print("--------", column1)
                obj = User.objects.filter(username= column1).first()
                obj.delete()

            else:
                print("Invalid row:", row)

    return render(request, 'dash_board.html')
