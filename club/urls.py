from . import views
from django.urls import path


urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('', views.HomePage.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.BookingPage.as_view(), name='booking'),
]