from datetime import datetime
from http.client import responses
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from app.forms import VenueForm ,EventForm
from . models import Events ,Venue
from django.http import HttpResponse
# Create your views here.

#Generate text file venue list
def venue_text(request):
    response = HttpResponse(content_type ='text/plain')
    response['Content-Disposition'] = 'attachment; file-name = venues.txt'
    #Designates the model
    venues = Venue.objects.all()
    #create blank list
    lines = []
    #loop through and output
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.Zip_code}')
    #write to text file
    response.writelines(lines)
    return response
    

#delete venue
def delete_venues(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect("list_venues")

#delete an event
def delete_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    event.delete()
    return redirect("list_events")

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event? submitted = True')
        else:
            form = EventForm()
            if 'submitted' in request.GET:
                submitted = True
                
    forms = EventForm()
    context = {
        'forms' : forms,
        'submitted' : submitted
    }
    return render(request ,'events/add_event.html',context )

def update_events(request,event_id):
    event = Events.objects.get(pk=event_id)
    form = EventForm(request.POST or None , instance = event )
    if form.is_valid():
        form.save()
        return redirect('list_events')
    return render(request,'events/update_event.html',{ "form" : form ,'event' : event})
    

def update_venues(request , venue_id):
    venue = Venue.objects.get(pk = venue_id)
    form = VenueForm(request.POST or None , instance =venue)
    if form.is_valid():
        form.save()
        return redirect("list_venues")
    return render(request, 'events/update_venue.html',{'venue' : venue , 'form' : form})
    


def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venue = Venue.objects.filter(name__contains = searched)
        return render(request,'events/search_venues.html',{'searched' : searched , 'venue' : venue })
    else:
         return render(request,'events/search_venues.html',{})


def show_venues(request, venue_id):
    venue = Venue.objects.get(pk =venue_id )
    context = { 'venue' : venue }
    return render(request,'events/venue_list.html' , context)
    

def list_venues(request):
    venue_list = Venue.objects.all()
    context = {
        'venue_list' : venue_list
    }
    return render(request,'events/venues_list.html', context)


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue? submitted = True')
        else:
            form = VenueForm()
            if 'submitted' in request.GET:
                submitted = True
                
    forms = VenueForm()
    context = {
        'forms' : forms,
        'submitted' : submitted
    }
    return render(request ,'events/venue.html',context )


def all_events(request):
    event_list = Events.objects.all()
    context = {
        'event_list' : event_list
    }
    return render(request , 'events/events_list.html', context)


def index(request , year=datetime.now().year , month=datetime.now().strftime('%B')): #months as locals full name
    name = "John"
    month = month.capitalize()
    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    #create a calendar
    
    cal = HTMLCalendar().formatmonth(year,month_number)
    
    #  get current year
    now = datetime.now()
    current_year = now.year
    
    #get current time
    time = now.strftime('%I:%M  %p')
    
    return render (request,'events/home.html', {
        'name' : name ,
        'year' : year ,
        'month' : month,
        'month_number' : month_number ,
        'cal' : cal,
        'current_year' : current_year,
        'time' : time
        
    })