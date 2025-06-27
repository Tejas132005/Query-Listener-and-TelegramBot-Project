from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import login
from django.contrib.auth.models import User 
from complaints.models import Ticket

class MainPage(APIView):
    def get(self, request):
        return render(request, 'accounts/main_page.html')

class RegisterAPI(APIView):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
        }

        if User.objects.filter(username=data['username']).exists():
            return render(request, 'accounts/register.html', {'error': 'Username already exists'})

        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()

            try:
                send_mail(
                    subject="Registration Successful",
                    message=f"Hello {user.username},\n\nThank you for registering with us!",
                    from_email="tejasjyoti2005@gmail.com",
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            except Exception as e:
                return HttpResponse(f"Email sending failed: {str(e)}")

            return redirect('login')
               
        return render(request, "accounts/register.html", {'errors': serializer.errors})


class LoginAPI(APIView):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        data = {
            'username' : request.POST.get('username'),
            'password' : request.POST.get('password'),
        }
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return redirect('dashboard')
        return render(request, 'accounts/login.html', {'errors' : serializer.errors})
