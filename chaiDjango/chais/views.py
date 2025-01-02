from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404


# Create your views here.
def all_chais(request):
    Chai =ChaiVarity.objects.all()
    return render(request,'chais/all_chais.html',{'Chai':Chai})

def chai_detail(request,chai_id):
    chai =get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'chais/chai_details.html',{'Chai' :chai})