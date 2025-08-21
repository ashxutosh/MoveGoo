from django.contrib import admin
from .models import Contact, Booking, Testimonial, TeamMember, CompanyInfo, Vehicle
import json
from django.utils.safestring import mark_safe

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    search_fields = ('subject', 'name', 'email')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'booking_date', 'formatted_details')
    list_filter = ('service_type',)
    search_fields = ('service_type',)

    def formatted_details(self, obj):
        details_str = json.dumps(obj.details, indent=2)
        return mark_safe(f'<pre>{details_str}</pre>')
    formatted_details.short_description = 'Booking Details'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('author',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'title')

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make_model', 'owner_name', 'vehicle_type', 'city')
    list_filter = ('vehicle_type', 'city')
    search_fields = ('make_model', 'owner_name')