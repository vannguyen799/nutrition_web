from django.shortcuts import render
from .models import User
from decorator import require_admin

# Create your views here.

@require_admin
def index(request):
    if request.method == 'GET':
        return render(request, 'admin/usermanage/index.html', {'users': User.objects.all()})
