from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['re_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email address already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1,
                                                email=email)

                user.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.warning(request, 'Both Passwords are not matched')
            return redirect('register')

    else:
        return render(request, 'register.html', {})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

def custom_500(request, exception):
    return render(request, "404.html", {})

def logout(request):
    auth.logout(request)
    return redirect('/')



