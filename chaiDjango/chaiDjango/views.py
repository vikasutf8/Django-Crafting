from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world , you are doning djang")
    return render(request,'website/index.html')
#rendering templates




def about(request):
    return HttpResponse("Hello world , you are about djang")


def contact(request):
    return HttpResponse("Hello world , you are contact djang")