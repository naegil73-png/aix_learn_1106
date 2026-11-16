from django.shortcuts import render

def index(request):
    if request.method == "POST":
        length = float(request.POST.get('length',''))
        width = float(request.POST.get('width',''))
        thick = float(request.POST.get('thick',''))

        