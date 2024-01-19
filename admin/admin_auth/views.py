from django.shortcuts import render, redirect
from django.contrib import messages

from .form import LoginForm
from .models import *


# Create your views here.

def login(request):
    if request.session.get('permission') == 'admin':
        return redirect('admin_dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = User.hash_password(request.POST['password'])

        try:
            user = User.objects.get(username=username, password=password)
            if user.permission.name.lower() == 'admin' and not user.is_locked:
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['email'] = user.email
                request.session['permission'] = user.permission.name.lower()

                # request.session['user'] = user
                user.is_active = True
                user.save()

                messages.success(request, 'Login successful.')
                print('login successful {}'.format(username))
                return redirect('admin_dashboard')
            messages.error(request, 'Dont have permission')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'admin/login.html', {'form': LoginForm()})


def logout(request):
    if 'user_id' in request.session:
        _logout(request)
        messages.success(request, 'Logout successful.')

    return redirect('admin_login')  # Redirect to your home page


def _logout(request):
    try:
        if request.session['user_id']:
            print(request.session['user_id'])
            user = User.objects.get(pk=request.session['user_id'])
            user.is_active = False
            user.save()
    except User.DoesNotExist:
        print('log out: user does not exist')
    del request.session['user_id']
    del request.session['username']
    del request.session['email']
    del request.session['permission']
    # del request.session['user']
