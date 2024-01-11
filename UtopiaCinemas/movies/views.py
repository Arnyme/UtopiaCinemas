from time import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Movie, Screening, Seat, Booking


class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie_list.html', {'movies': movies})


class MovieDetailView(View):
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movie_detail.html', {'movie': movie})


class ScreeningListView(View):
    def get(self, request):
        screenings = Screening.objects.all()
        return render(request, 'screening_list.html', {'screenings': screenings})


class ScreeningDetailView(View):
    def get(self, request, screening_id):
        screening = get_object_or_404(Screening, pk=screening_id)
        return render(request, 'screening_detail.html', {'screening': screening})


def make_booking(request, screening_id):
    screening = get_object_or_404(Screening, pk=screening_id)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('selected_seats')
        total_price = calculate_total_price(selected_seats, screening)

        # Create a new booking
        booking = Booking.objects.create(
            user=request.user,
            screening=screening,
            total=total_price
        )
        booking.seats.set(selected_seats)

        # Update seat status to booked
        Seat.objects.filter(pk__in=selected_seats).update(status='Booked')

        return redirect('booking_detail', booking_id=booking.id)

    seats = screening.seats.filter(status='Available')
    return render(request, 'make_booking.html', {'screening': screening, 'seats': seats})


def calculate_total_price(selected_seats, screening):
    # Implement dynamic pricing logic here
    # This is a simplified example. You can adjust based on your specific requirements.
    base_price = screening.base_price
    current_time = timezone.localtime(timezone.now())  # Convert to local timezone

    # Check if the screening is during peak hours (e.g., evenings)
    if current_time.hour >= 18:
        return base_price * 1.2  # Increase the price by 20% for evening screenings
    else:
        return base_price  # Keep the base price for non-peak screenings
