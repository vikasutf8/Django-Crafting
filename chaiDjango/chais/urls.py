

from django.urls import path
from . import views
#localhost:8000/chais/
#localhost:8000/chais/order

urlpatterns = [
    
    path('',views.all_chais ,name='Chais-home'),
 
    path('<int:chai_id>/',views.chai_detail ,name='Chai_details'),
    

]
