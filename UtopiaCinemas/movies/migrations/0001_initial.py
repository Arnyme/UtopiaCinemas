# Generated by Django 5.0.1 on 2024-01-12 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('seats', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='movies/movies_images')),
                ('rating', models.FloatField()),
                ('reviews', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('auditorium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenings', to='movies.auditorium')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenings', to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('position', models.IntegerField()),
                ('type', models.CharField(choices=[('VIP', 'VIP'), ('Regular', 'Regular')], max_length=10)),
                ('status', models.CharField(choices=[('Booked', 'Booked'), ('Available', 'Available')], max_length=10)),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='movies.screening')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('coupon', models.CharField(blank=True, max_length=10, null=True)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='movies.screening')),
                ('seats', models.ManyToManyField(related_name='bookings', to='movies.seat')),
            ],
        ),
    ]
