from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login successful for user:", username)
            return redirect('dashboard:dashboard')  
        else:
            print("Login failed for user:", username)
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')    