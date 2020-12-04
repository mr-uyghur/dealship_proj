from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.home, name = "home"),
    path('about', views.about, name = "about"),
    path('services', views.services, name = "services"),
    path('contact', views.contact, name = "contact"),
    
]