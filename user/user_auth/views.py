from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

from .form import RegisterForm
# Create your views here.

def login(request):
    if request.session.get('user_id') is not None:
        return redirect('user:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = User.hash_password(request.POST.get('password'))
        try:
            # print(f"{username}/{request.POST.get('password')}")
            user = User.objects.get(username=username, password=password)

            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['email'] = user.email
            request.session['permission'] = user.permission.name.lower()
            # request.session['user'] = user
            # user.objects.update(is_active=1)
            messages.success(request, 'Login successful.')
            return redirect('user:home')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user/signin.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(form.is_valid())
        # print(form.cleaned_data )
        if form.is_valid():
            try:
                user = User.objects.create(
                    username=form.cleaned_data.get('username'),
                    password=User.hash_password(form.cleaned_data.get('password')),
                    email=form.cleaned_data.get('email'),
                    permission_id=1,
                    firstname=form.cleaned_data.get('firstname'),
                    lastname=form.cleaned_data.get('lastname')
                )
                return login(request)
            except Exception as e:
                messages.error(e, 'Invalid username or password.')
        else:
            messages.error(request, 'Dữ liệu không hợp lệ')
            return render(request, 'user/signin.html', {'form': form})


def logout(request):
    if 'user_id' in request.session:
        _logout(request)
    return redirect(to='user:home')  # Redirect to your home page



def _logout(request):
    try:
        User.objects.get(pk=request.session['user_id']).objects.update(is_active=False)
    except Exception:
        pass
    try:
        del request.session['user_id']
        del request.session['username']
        del request.session['email']
        del request.session['permission']
        del request.session['user']
    except KeyError:
        pass


