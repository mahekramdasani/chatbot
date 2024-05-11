from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect, render

from .models import Chat, CustomUser
from .serializers import ChatSerializer, UserSerializer


def home(request):
    return render(request,'home.html')

def user_registration(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            if CustomUser.objects.filter(username=serializer.validated_data['email']).exists():
                return render(request, 'register.html', {"message": "Email already exists. Please choose a different one."})
            
            # Include the password when creating the user
            user = CustomUser.objects.create_user(username = request.POST['username'],email=request.POST['email'], password=request.POST['password'])
            user.save()
            # Automatically log in the user after registration
            login(request, user)
            return redirect('chat')
            
        return render(request, 'register.html', {"errors": serializer.errors})
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to chat.html after successful login
            return redirect('chat')
        else:
            return render(request, 'login.html', {"message": "Invalid email or password."})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    # user = request.user
    logout(request)
    return redirect('/')

@login_required
def chat_interaction(request):
    if request.method == 'POST':
        
        user = request.user  
        message = request.POST.get('message')
        
        # Check token balance
        if user.tokens < 100:
            chat_history = Chat.objects.filter(user=user).order_by("-timestamp")
            chat_history_serializer = ChatSerializer(chat_history, many=True)

            return render(request, 'chat.html', {"message": "Insufficient tokens to ask a question.","chat_history":chat_history_serializer.data})
        
        # Deduct 100 tokens for each question asked
        user.tokens -= 100
        user.save()

        # For simplicity, let's assume a dummy response
        response = "Dummy response"

        # Save the chat history
        chat = Chat.objects.create(user=user, message=message, response=response)
        serializer = ChatSerializer(chat)

        # Get all chat history for the user
        chat_history = Chat.objects.filter(user=user).order_by("-timestamp")
        chat_history_serializer = ChatSerializer(chat_history, many=True)

        return render(request, 'chat.html', { "chat_history": chat_history_serializer.data})
    return render(request,'chat.html')


def token_balance(request):
    user = request.user
    return render(request, 'balance.html', {"tokens": user.tokens})
