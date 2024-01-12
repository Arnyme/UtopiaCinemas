from django.contrib import admin
from .models import Movie
#
#
# class GenreAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'release_date', 'image_url')
#     search_fields = ('title', 'synopsis')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'price', 'rating', 'image')


#
# class SeatTypeAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# class SeatAdmin(admin.ModelAdmin):
#     list_display = ('row', 'number', 'seat_type', 'available')
#     list_filter = ('seat_type', 'available')
#
#
# class BranchAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# class CinemaHallAdmin(admin.ModelAdmin):
#     list_display = ('name', 'branch', 'capacity')
#     list_filter = ('branch',)
#
#
# class ShowtimeAdmin(admin.ModelAdmin):
#     list_display = ('movie', 'date', 'time', 'cinema_hall')
#     list_filter = ('movie', 'cinema_hall')
#
#
# class PriceListAdmin(admin.ModelAdmin):
#     list_display = ('seat_type', 'day', 'price')
#     list_filter = ('seat_type', 'day')
#
#
# class TicketAdmin(admin.ModelAdmin):
#     list_display = ('showtime', 'user', 'price', 'status', 'booking_time')
#     list_filter = ('showtime', 'user', 'status')
#     readonly_fields = ('booking_time',)  # Make booking_time read-only
#
#
# # Register all models for the admin interface
# admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
# admin.site.register(SeatType, SeatTypeAdmin)
# admin.site.register(Seat, SeatAdmin)
# admin.site.register(Branch, BranchAdmin)
# admin.site.register(CinemaHall, CinemaHallAdmin)
# admin.site.register(Showtime, ShowtimeAdmin)
# admin.site.register(PriceList, PriceListAdmin)
# admin.site.register(Ticket, TicketAdmin)
