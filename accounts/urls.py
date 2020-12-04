from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('login', views.login, name = "login"),
    path('register', views.register, name = "register"),
    path('logout', views.logout, name = "logout"),
    path('dashboard', views.dashboard, name = "dashboard"),
]