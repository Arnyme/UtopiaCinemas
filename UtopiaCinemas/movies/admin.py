from django.contrib import admin
from .models import Movie, Auditorium, Screening, Seat, Booking


class ScreeningInline(admin.TabularInline):
    model = Screening
    extra = 1


class SeatInline(admin.TabularInline):
    model = Seat
    extra = 1


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'release_date', 'price', 'rating')
    search_fields = ('title', 'genre', 'language')
    inlines = [ScreeningInline]


class AuditoriumAdmin(admin.ModelAdmin):
    list_display = ('name', 'seats', 'location')
    search_fields = ('name', 'location')


class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('movie', 'auditorium', 'start_time', 'base_price')
    search_fields = ('movie__title', 'auditorium__name')
    inlines = [SeatInline]


class SeatAdmin(admin.ModelAdmin):
    list_display = ('row', 'position', 'type', 'status', 'screening')
    list_filter = ('type', 'status')
    search_fields = ('screening__movie__title',)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'screening', 'total', 'is_paid', 'is_cancelled', 'created_at', 'updated_at')
    list_filter = ('is_paid', 'is_cancelled')
    search_fields = ('user__username', 'screening__movie__title')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Auditorium, AuditoriumAdmin)
admin.site.register(Screening, ScreeningAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Booking, BookingAdmin)
