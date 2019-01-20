from django.urls import path
from . import views

#in main urls.py we are directing all /listings/  to theses urls 
urlpatterns = [
    path('', views.index, name='listings'),  #will calll index on listings views /listings
    path('<int:listing_id>', views.listing, name='listing'), # /listings/id
    path('search', views.search, name='search') # listings/search
]