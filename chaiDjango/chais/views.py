from django.shortcuts import render

# Create your views here.
def all_chais(request):
    return render(request,'chais/all_chais.html')

def order_chais(request):
    return render(request,'chais/all_chais.html')