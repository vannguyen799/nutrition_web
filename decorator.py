from django.shortcuts import redirect


def require_admin(func):
    def wrapper(request, *args, **kwargs):
        try:
            if request.session['permission'] == 'admin':
                return func(request, *args, **kwargs)
        except KeyError:
            pass
        return redirect('admin_login')

    return wrapper


def require_login(func):
    def wrapper(request, *args, **kwargs):
        if not request.session['user_id']:
            return func(request, *args, **kwargs)
        else:
            return redirect('user_login')

    return wrapper
