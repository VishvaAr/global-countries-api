from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This tells Django: "For everything else, check the firstApp urls"
    path('', include('firstApp.urls')), 
]