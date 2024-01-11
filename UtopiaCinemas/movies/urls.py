from django.urls import path
from .views import MovieListView, MovieDetailView, ScreeningListView, ScreeningDetailView, make_booking

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:movie_id>/', MovieDetailView.as_view(), name='movie_detail'),
    path('screenings/', ScreeningListView.as_view(), name='screening_list'),
    path('screenings/<int:screening_id>/', ScreeningDetailView.as_view(), name='screening_detail'),
    path('make-booking/<int:screening_id>/', make_booking, name='make_booking'),
    # Add more paths as needed
]
