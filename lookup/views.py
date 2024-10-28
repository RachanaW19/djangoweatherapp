from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})  
    # here we rendered the request which is pointing towards home.html

def about(request):
    return render(request, 'about.html', {})