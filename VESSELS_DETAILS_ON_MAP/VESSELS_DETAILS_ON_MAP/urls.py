from django.urls import path
from django.contrib import admin
from VESSELS_DETAILS_APP.views import show_route_details

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', show_route_details, name='show_route_details'),
    
]
