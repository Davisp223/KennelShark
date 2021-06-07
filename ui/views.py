from django.shortcuts import render

# Create your views here.

def ui(request):
    return render(request, 'ui/index.html')