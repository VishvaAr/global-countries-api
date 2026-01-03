from django.urls import path 
from firstApp import views 

urlpatterns = [
    # Match 'api/countries' to the 'countries_list' function in views.py
    path('api/countries', views.countries_list), 
    
    # Match 'api/countries/123' to the 'countries_detail' function
    path('api/countries/<int:pk>', views.countries_detail),
]