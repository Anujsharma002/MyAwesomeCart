from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="Aboutus"),
    path('contact',views.contact,name="Contactus"),
    path('tracker/',views.tracker,name="trackingStatus"),
    path('search',views.search,name="Search"),
    path('product/<int:myid>',views.productView,name="ProductView"),
    path('checkout',views.checkout,name="Checkout")
]
