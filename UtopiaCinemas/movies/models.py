# Import the models module from django.db
from django.db import models

# Import the User model from django.contrib.auth.models
from django.contrib.auth.models import User


# Define the Movie model
class Movie(models.Model):
    # Define the fields for the Movie model
    title = models.CharField(max_length=100)  # The title of the movie
    genre = models.CharField(max_length=50)  # The genre of the movie
    language = models.CharField(max_length=50)  # The language of the movie
    release_date = models.DateField()  # The release date of the movie
    price = models.DecimalField(max_digits=6, decimal_places=2)  # The price of the movie ticket
    image = models.ImageField(upload_to='movies')  # The image of the movie poster
    rating = models.FloatField()  # The average rating of the movie
    reviews = models.TextField()  # The reviews of the movie

    # Define the string representation of the Movie model
    def __str__(self):
        return self.title


# Define the Auditorium model
class Auditorium(models.Model):
    # Define the fields for the Auditorium model
    name = models.CharField(max_length=50)  # The name of the auditorium
    seats = models.IntegerField()  # The number of seats in the auditorium
    location = models.CharField(max_length=100)  # The location of the auditorium

    # Define the string representation of the Auditorium model
    def __str__(self):
        return self.name


# Define the Screening model
class Screening(models.Model):
    # Define the fields for the Screening model
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings')  # The movie that is screened
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE,
                                   related_name='screenings')  # The auditorium where the movie is screened
    start_time = models.DateTimeField()  # The start time of the screening
    base_price = models.DecimalField(max_digits=6, decimal_places=2)  # Initial price of the screening

    # Define the string representation of the Screening model
    def __str__(self):
        return f'{self.movie.title} - {self.auditorium.name} - {self.start_time}'


# Define the Seat model
class Seat(models.Model):
    # Define the fields for the Seat model
    row = models.IntegerField()  # The row number of the seat
    position = models.IntegerField()  # The position of the seat within the row
    type = models.CharField(max_length=10, choices=[('VIP', 'VIP'), ('Regular', 'Regular')])  # The type of the seat
    status = models.CharField(max_length=10,
                              choices=[('Booked', 'Booked'), ('Available', 'Available')])  # The status of the seat
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE,
                                  related_name='seats')  # The screening that the seat belongs to

    # Define the string representation of the Seat model
    def __str__(self):
        return f'{self.row}-{self.position} - {self.type} - {self.status}'


# Define the Booking model
class Booking(models.Model):
    # Define the fields for the Booking model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')  # The user who made the booking
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE,
                                  related_name='bookings')  # The screening that the booking is for
    seats = models.ManyToManyField(Seat, related_name='bookings')  # The seats that the booking includes
    total = models.DecimalField(max_digits=6, decimal_places=2)  # The total amount of the booking
    coupon = models.CharField(max_length=10, blank=True,
                              null=True)  # The coupon code that the user applied to the booking
    discount = models.DecimalField(max_digits=6, decimal_places=2,
                                   default=0)  # The discount amount that the user received from the coupon
    is_paid = models.BooleanField(default=False)  # The payment status of the booking
    is_cancelled = models.BooleanField(default=False)  # The cancellation status of the booking
    created_at = models.DateTimeField(auto_now_add=True)  # The creation date and time of the booking
    updated_at = models.DateTimeField(auto_now=True)  # The update date and time of the booking

    # Define the string representation of the Booking model
    def __str__(self):
        return f'{self.user.username} - {self.screening} - {self.total}'
