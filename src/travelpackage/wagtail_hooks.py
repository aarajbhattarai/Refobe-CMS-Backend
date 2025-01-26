

from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import TravelPackage,Booking

class TravelPackageSnippetViewSet(SnippetViewSet):
    model = TravelPackage
    icon = "globe"  # change as required
    add_to_admin_menu = True
    menu_label = "Travel Packages"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ["title", "base_price","duration_days"]
    search_fields = ("name",)
    
    
register_snippet(TravelPackageSnippetViewSet)

class BookingSnippetViewSet(SnippetViewSet):
    model = Booking
    icon = "calendar-alt"  # change as required
    add_to_admin_menu = True
    menu_label = "Bookings"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ["package","name","total_price", "booking_start_date","number_of_people","phone"]
    search_fields = ("name",)
    
    
register_snippet(BookingSnippetViewSet)



