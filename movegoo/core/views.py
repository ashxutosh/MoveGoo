from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking, Testimonial, TeamMember, Contact, CompanyInfo, Vehicle
from .forms import ContactForm, VehicleForm

# --- Main Page Views ---

def home(request):
    """
    Handles the display of the home page.
    Fetches all active testimonials from the database to be displayed dynamically.
    """
    testimonials = Testimonial.objects.filter(is_active=True)
    context = {'testimonials': testimonials}
    return render(request, 'home.html', context)

def about(request):
    """
    Renders the about page.
    Fetches all active team members to be displayed dynamically.
    """
    team_members = TeamMember.objects.filter(is_active=True)
    context = {'team_members': team_members}
    return render(request, 'about.html', context)

def services(request):
    """Renders the main services page."""
    return render(request, 'service.html')

def contact(request):
    """
    Handles both displaying the contact page and processing the contact form.
    Fetches dynamic company information to display on the page.
    """
    company_info = CompanyInfo.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! Our team will get back to you shortly.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'company_info': company_info
    }
    return render(request, 'contact.html', context)

# --- Booking and Form Handling Views ---

def car_rental(request):
    """Handles the car rental booking form."""
    if request.method == 'POST':
        details = {
            'pickup_location': request.POST.get('pickup-location'),
            'pickup_date': request.POST.get('pickup-date'),
            'return_date': request.POST.get('return-date'),
        }
        Booking.objects.create(service_type='Car Rental', details=details)
        messages.success(request, 'Thank you for your request! Our team will contact you in 1-2 hours.')
        return redirect('home')
    return render(request, 'car_rental.html')

def driver_service(request):
    """Handles the driver service booking form."""
    if request.method == 'POST':
        details = {
            'service_location': request.POST.get('service-location'),
            'service_date': request.POST.get('service-date'),
            'duration': request.POST.get('duration'),
        }
        Booking.objects.create(service_type='Driver Service', details=details)
        messages.success(request, 'Thank you for your request! Our team will contact you in 1-2 hours.')
        return redirect('home')
    return render(request, 'driver_service.html')

def logistic(request):
    """Handles the logistics quote form."""
    if request.method == 'POST':
        details = {
            'origin': request.POST.get('origin'),
            'destination': request.POST.get('destination'),
            'shipment_date': request.POST.get('shipment-date'),
        }
        Booking.objects.create(service_type='Logistics', details=details)
        messages.success(request, 'Thank you for your request! Our team will contact you in 1-2 hours.')
        return redirect('home')
    return render(request, 'logistic.html')

def flight_ticket(request):
    """Handles the flight ticket search form."""
    if request.method == 'POST':
        details = {
            'from': request.POST.get('from'),
            'to': request.POST.get('to'),
            'departure_date': request.POST.get('departure-date'),
        }
        Booking.objects.create(service_type='Flight Ticket', details=details)
        messages.success(request, 'Thank you for your request! Our team will contact you in 1-2 hours.')
        return redirect('home')
    return render(request, 'flight_ticket.html')

def bus_ticket(request):
    """Handles the bus ticket search form."""
    if request.method == 'POST':
        details = {
            'from_city': request.POST.get('from-city'),
            'to_city': request.POST.get('to-city'),
            'travel_date': request.POST.get('travel-date'),
        }
        Booking.objects.create(service_type='Bus Ticket', details=details)
        messages.success(request, 'Thank you for your request! Our team will contact you in 1-2 hours.')
        return redirect('home')
    return render(request, 'bus_ticket.html')

def train_ticket(request):
    """Handles the train ticket search form."""
    if request.method == 'POST':
        details = {
            'from_station': request.POST.get('from-station'),
            'to_station': request.POST.get('to-station'),
            'travel_date': request.POST.get('travel-date'),
        }
        Booking.objects.create(service_type='Train Ticket', details=details)
        messages.success(request, 'Thank you for your request! Our team will contact you in 1-2 hours.')
        return redirect('home')
    return render(request, 'train_ticket.html')

def vehicle_listing(request):
    """Handles the vehicle listing form."""
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for listing your vehicle! We will review it and get back to you shortly.')
            return redirect('vehicle_listing')
    else:
        form = VehicleForm()
    
    context = {'form': form}
    return render(request, 'vehicle_listing.html', context)

# --- Legal/Policy Page Views ---

def privacy_policy(request):
    """Renders the privacy policy page."""
    return render(request, 'privacy_policy.html')

def terms_of_services(request):
    """Renders the terms of service page."""
    return render(request, 'terms_of_services.html')

def cookie_policy(request):
    """Renders the cookie policy page."""
    return render(request, 'cookie_policy.html')
