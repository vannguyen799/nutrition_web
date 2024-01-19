from django.shortcuts import render

from decorator import require_admin


# Create your views here.
@require_admin
def index(request):
    return render(request, 'admin/dashboard/dashboard.html')