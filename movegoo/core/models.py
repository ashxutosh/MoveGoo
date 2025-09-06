from django.db import models

# Model for all booking requests from the forms on the home page
class Booking(models.Model):
    """
    Stores submissions from the various booking forms in the home page widget.
    """
    SERVICE_TYPES = [
        ('Car Rental', 'Car Rental'),
        ('Driver Service', 'Driver Service'),
        ('Logistics', 'Logistics'),
        ('Flight Ticket', 'Flight Ticket'),
        ('Bus Ticket', 'Bus Ticket'),
        ('Train Ticket', 'Train Ticket'),
    ]
    
    service_type = models.CharField(
        max_length=20, 
        choices=SERVICE_TYPES,
        help_text="The type of service requested by the user."
    )
    
    details = models.JSONField(
        help_text="A JSON object containing the specific details from the submitted form."
    )
    
    booking_date = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the booking was submitted."
    )

    def __str__(self):
        return f"{self.service_type} booking on {self.booking_date.strftime('%Y-%m-%d')}"

# Model will store the dynamic testimonials for the home page
class Testimonial(models.Model):
    """
    Represents a customer testimonial to be displayed on the home page.
    """
    author = models.CharField(
        max_length=100,
        help_text="The name of the customer giving the testimonial."
    )
    
    quote = models.TextField(
        help_text="The content of the testimonial."
    )
    
    rating = models.IntegerField(
        default=5, 
        help_text="Rating from 1 to 5 stars."
    )
    
    image_url = models.URLField(
        max_length=255, 
        blank=True, 
        null=True,
        help_text="URL to the author's profile picture."
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Only active testimonials will be shown on the site."
    )

    def __str__(self):
        return f"Testimonial by {self.author}"

# Model for the dynamic team section on the about page
class TeamMember(models.Model):
    """
    Represents a team member to be displayed on the about page.
    """
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.title}"


#dynamic contact info and business hours
class CompanyInfo(models.Model):
    """
    Stores the main contact and business information for the site.
    It's intended to have only one entry.
    """
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=60)
    email = models.EmailField()
    shift_1_hours = models.CharField(max_length=50)
    shift_2_hours = models.CharField(max_length=50)

    def __str__(self):
        return "Company Information"
    

class Vehicle(models.Model):
    """
    Stores information about vehicles listed by users to rent out.
    """
    VEHICLE_TYPES = [
        ('Car (Sedan, Hatchback)', 'Car (Sedan, Hatchback)'),
        ('SUV / MUV', 'SUV / MUV'),
        ('Van / Minibus', 'Van / Minibus'),
        ('Truck', 'Truck'),
        ('Trolley / Trailer', 'Trolley / Trailer'),
        ('Construction (e.g., JCB)', 'Construction (e.g., JCB)'),
        ('Other Commercial Vehicle', 'Other Commercial Vehicle'),
    ]
    owner_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100, choices=VEHICLE_TYPES)
    make_model = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make_model} listed by {self.owner_name}"



class Contact(models.Model):
    """
    Stores submissions from the main contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"