from django.shortcuts import redirect, render


def _redirect_method_not_allowed(request, accepted_method):
    return render(request, template_name='blank.html', context={'content': '_redirect_method_not_allowed'})

    pass


def _redirect_missing_field(request, required_field):
    return render(request, template_name='blank.html', context={'content': '_redirect_method_not_allowed'})
    pass


class require:
    @staticmethod
    def admin(func):
        def wrapper(request, *args, **kwargs):
            try:
                if request.session['permission'] == 'admin':
                    return func(request, *args, **kwargs)
            except KeyError:
                pass
            return redirect('admin_login')

        return wrapper

    @staticmethod
    def login(func):
        def wrapper(request, *args, **kwargs):
            if not request.session['user_id']:
                return func(request, *args, **kwargs)
            else:
                return redirect('user_login')

        return wrapper

    @staticmethod
    def method(*accept_method):
        for method_ in accept_method:
            method_ = method_.upper()

        def decorator(func):
            def wrapper(request, *args, **kwargs):
                if request.method not in accept_method:
                    return _redirect_method_not_allowed(request=request, accepted_method=accept_method)
                return func(request, *args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def post_form(*field_name):
        return require._require_field('POST', field_name)

    @staticmethod
    def get_form(*field_name):
        return require._require_field('GET', field_name)

    @staticmethod
    def delete_form(*field_name):
        return require._require_field('DELETE', field_name)

    @staticmethod
    def put_form(*field_name):
        return require._require_field('PUT', field_name)

    @staticmethod
    def _require_field(method, *field_name):
        def decorator(func):
            def wrapper(request, *args, **kwargs):
                if request.method == method.upper():
                    params = None
                    # match request.method:
                    #     case 'POST':
                    #         params = request.POST
                    #     case 'GET':
                    #         params = request.GET
                    #     case 'PUT':
                    #         params = request.PUT
                    #     case 'DELETE':
                    #         params = request.DELETE

                    for name in field_name:
                        if name not in params:
                            return _redirect_missing_field(request=request, required_field=field_name)
                return func(request, *args, **kwargs)

            return wrapper

        return decorator
