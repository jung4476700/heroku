from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def study2(request):
    return render(request, 'study2.html')