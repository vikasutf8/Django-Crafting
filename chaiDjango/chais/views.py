from django.shortcuts import render
from .models import ChaiVarity,Store
from django.shortcuts import get_object_or_404
from .form import ChaiVarityform

# Create your views here.
def all_chais(request):
    Chai =ChaiVarity.objects.all()
    return render(request,'chais/all_chais.html',{'Chai':Chai})

def chai_detail(request,chai_id):
    chai =get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'chais/chai_details.html',{'Chai' :chai})

def chai_store_view(request):
    stores =None
    if request.method == 'POST':
        form =ChaiVarityform(request.POST)
        if(form.is_valid()):
            chai_variety =form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties = chai_variety)
    else:
        form= ChaiVarityform()
    return render(request,"chai/Chai_store.html",{'stores' :stores, 'form' :form}),
# always form send 