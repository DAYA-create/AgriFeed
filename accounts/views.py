

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models  import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

#registration view
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(
            username = username,
            email = email,
            password = password
        )
        return redirect('login')
    return render(request, 'register.html')
#login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
#logout view
def logout_view(request):
    logout(request)
    return redirect('login')
#dashboard,..To view dashboard - Login must be done
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')