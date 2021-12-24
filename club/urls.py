from . import views
from django.urls import path


urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('', views.HomePage.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('manage/', views.ManageBooking.as_view(), name='manage'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),
]