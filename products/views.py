from django.shortcuts import render

def seller_dashboard(request):
    return render(request, 'products/seller/dashboard.html')