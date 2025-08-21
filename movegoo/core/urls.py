from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),

    # Service pages (for form submissions and direct visits)
    path('car-rental/', views.car_rental, name='car_rental'),
    path('driver-service/', views.driver_service, name='driver_service'),
    path('logistic/', views.logistic, name='logistic'),
    path('flight-ticket/', views.flight_ticket, name='flight_ticket'),
    path('bus-ticket/', views.bus_ticket, name='bus_ticket'),
    path('train-ticket/', views.train_ticket, name='train_ticket'),
    path('vehicle-listing/', views.vehicle_listing, name='vehicle_listing'),

    # Legal/Policy pages
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-services/', views.terms_of_services, name='terms_of_services'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
]