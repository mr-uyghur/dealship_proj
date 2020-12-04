from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.cars, name = "cars"),
    path('<int:id>', views.car_detail, name = "car_detail"),
    path('search', views.search, name = "search")
    
]