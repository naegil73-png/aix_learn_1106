from django.shortcuts import render

def blist(request):
    if request.method == 'GET':
        return render(request, 'board.html')


# def msearch(request):
#     if request.method == 



# def mview(request):
