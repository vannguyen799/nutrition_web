from django.shortcuts import render
from .models import User
from decorator import require


# Create your views here.

@require.admin
def index(request):
    if request.method == 'GET':
        return render(request, 'admin/usermanage/index.html', {'users': User.objects.all()})


@require.admin
def lock_user(request):
    pass



@require.admin
def unlock_user(request):
    pass


@require.admin
def add_user(request):
    pass


@require.admin
def edit_user(request):
    pass
