from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.conf import settings
from django.shortcuts import render

def custom_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/')
    else:
        logout(request)
        # Return an 'invalid login' error message.
        return redirect('/loginpage/')


def do_logout(request):
    logout(request)
    return redirect('/loginpage/')
