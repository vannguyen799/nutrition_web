from django.shortcuts import render

from decorator import require


# Create your views here.
@require.admin
def index(request):
    return render(request, 'admin/dashboard/dashboard.html')