

from django.urls import path
from . import views
#localhost:8000/chais/
#localhost:8000/chais/order

urlpatterns = [
    
    path('',views.all_chais ,name='Chais-home'),
    path('order/',views.order_chais ,name='Chais-Order'),
    

]
