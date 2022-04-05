from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'home'),
    path('<int:year>/<str:month>/', views.index , name = 'home'),
    path('event/',views.all_events, name = 'list_events'),
    path('add_venue/',views.add_venue, name = 'add_venue'),
    path('list_venues/',views.list_venues, name = 'list_venues'),
    path('show_venues/<venue_id>',views.show_venues, name = 'show_venues'),
    path('search_venues/',views.search_venues, name = 'search_venues'),
    path('update_venues/<venue_id>',views.update_venues, name = 'update_venues'),
    path('update_events/<event_id>',views.update_events, name = 'update_events'),
    path('add_event/',views.add_event, name = 'add_event'),
    path('delete_event/<event_id>',views.delete_event, name = 'delete_event'),
    path('delete_venues/<venue_id>',views.delete_venues, name = 'delete_venues'),
    path('venue_text/',views.venue_text, name = 'venue_text'),



]
