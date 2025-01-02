
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ,name='home'),
    path('about/',views.about ,name='about'),
    path('contact/',views.contact ,name='contact'),
    path('chai/',include('chais.urls'))  ,# now control tolly transfer to app



# this path for auto reload always at end
    path("__reload__/",include("django_browser_reload.urls")),
]
