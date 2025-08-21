from django import forms
from .models import Contact, Vehicle

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email', 'required': True}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message', 'rows': 6, 'required': True}),
        }

#vehicle listing page
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['owner_name', 'vehicle_type', 'make_model', 'city']
        widgets = {
            'owner_name': forms.TextInput(attrs={'placeholder': 'Your Name', 'required': True}),
            'vehicle_type': forms.Select(attrs={'required': True}),
            'make_model': forms.TextInput(attrs={'placeholder': 'e.g., Toyota Innova', 'required': True}),
            'city': forms.TextInput(attrs={'placeholder': 'Your City', 'required': True}),
        }
