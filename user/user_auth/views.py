from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *


# Create your views here.

def login(request):
    if request.session['user_id']:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = User.hash_password(request.POST['password'])

        try:
            user = User.objects.get(username=username, password=password)
            if not user.is_locked:
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['email'] = user.email
                request.session['permission'] = user.permission.name.lower()
                request.session['user'] = user
                user.objects.update(is_active=True)
                messages.success(request, 'Login successful.')
                return redirect('home')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user/login.html')


def register(request):
    pass


def logout(request):
    if 'user_id' in request.session:
        _logout(request)
        messages.success(request, 'Logout successful.')

    return redirect('home')  # Redirect to your home page



def _logout(request):
    User.objects.get(id=request.session['user_id']).objects.update(is_active=False)
    del request.session['user_id']
    del request.session['username']
    del request.session['email']
    del request.session['permission']
    del request.session['user']
