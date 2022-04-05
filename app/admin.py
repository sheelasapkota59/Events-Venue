from django.contrib import admin
from .models import Venue
from . models import MyClubUser
from . models import Events
# Register your models here.

#admin.site.register(Venue , VenueAdmin)
admin.site.register(MyClubUser)
#admin.site.register(Events)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name' , 'address','phone_number')
    ordering = ('name',) #this is tuple , it will put in order based on name
    search_fields = ('name' , 'address') #change the search bar of admin pannell
    
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date' , 'description', 'manager')
    list_display = ('name' , 'event_date','venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',) 
    