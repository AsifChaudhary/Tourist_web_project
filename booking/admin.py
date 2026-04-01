from django.contrib import admin
from .models import Destination, Booking

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_person', 'duration_days', 'is_featured')
    search_fields = ('title', 'location')
    list_filter = ('is_featured',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'number_of_people', 'total_price', 'status', 'booking_date')
    search_fields = ('user__username', 'destination__title')
    list_filter = ('status',)

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Booking, BookingAdmin)
