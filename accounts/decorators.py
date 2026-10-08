from django.contrib.auth.decorators import user_passes_test

def vendedor_required(view_func):
    return user_passes_test(
        lambda u: u.is_authenticated and u.es_vendedor,
        login_url='login'
    )(view_func)