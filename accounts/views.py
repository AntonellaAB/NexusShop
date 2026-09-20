from django.shortcuts import render
def home(request):
    return render(request, 'accounts/index.html')
# Create your views here.
