from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# C:\PHITRON\SOFTWARE-DEV-PROJECT\DjanGo_codes\project_2\templates\index.html
def index(request):
    return render(request, 'index.html')