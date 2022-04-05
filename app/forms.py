from multiprocessing import Event
from django import forms
from django.forms import ModelForm
from . models import Venue ,Events
 
class VenueForm(ModelForm):
     class Meta:
         model = Venue
         fields = ('name','address','Zip_code','phone_number','email_address','venue_image')
         labels = {
              'name': '' ,
             'address' : '' ,
             'Zip_code':  '' ,
             'phone_number': '' ,
             'web':  '' ,
             'email_address': '' ,
             'venue_image' : ''
         }
            
         widgets = {
             'name': forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder': 'Venue Name'}),
             'address' :  forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'Venue Address'}) ,
             'Zip_code':  forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Zip code' }) ,
             'phone_number':  forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder':  'Phone Number'}) ,
             'web':  forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'Website URL'}) ,
             'email_address':  forms.EmailInput(attrs = {'class' : 'form-control' ,'placeholder': 'Email Address'})
             
         }
         
class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'event_date','venue' ,'manager','description','attendees')
        labels = {
              'name': '' ,
             'event_date' : 'YYYY-MM-DD HH-MM:SS' ,
             'venue':  'Venue' ,
             'manager': 'Manager' ,
             'description':  '' ,
             'attendees': '' 
         }
            
        widgets = {
             'name': forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder': 'Venue Name'}),
             'event_date' :  forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'Event Date'}) ,
             'venue':  forms.Select(attrs = {'class' : 'form-select', 'placeholder': 'Venue' }) ,
             'manager':  forms.Select(attrs = {'class' : 'form-select' ,'placeholder':  'Admin'}) ,
             'description':  forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'About Venue'}) ,
             'attendees':  forms.SelectMultiple(attrs = {'class' : 'form-control' ,'placeholder': 'Atttendees'})
             
         }