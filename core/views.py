from django.shortcuts import render

def asosiy(request):
    return render(request, 'index.html')

def ferrari(request):
    return render(request, 'cars1.html')

def mersedes(request):
    return render(request, 'cars2.html')

def bmv(request):
    return render(request, 'cars3.html')

def toyota(request):
    return render(request, 'cars4.html')

def lada(request):
    return render(request, 'cars5.html')

def nissan(request):
    return render(request, 'cars6.html')