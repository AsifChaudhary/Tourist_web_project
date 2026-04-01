from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Destination, Booking

def home(request):
    featured_destinations = Destination.objects.filter(is_featured=True)[:3]
    return render(request, 'booking/home.html', {'featured_destinations': featured_destinations})

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'booking/destinations.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'booking/destination_detail.html', {'destination': destination})

@login_required
def book_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        number_of_people = request.POST.get('number_of_people')
        if number_of_people and int(number_of_people) > 0:
            booking = Booking(
                user=request.user,
                destination=destination,
                number_of_people=int(number_of_people)
            )
            booking.save()
            return redirect('dashboard')
    
    return render(request, 'booking/book_destination.html', {'destination': destination})

@login_required
def dashboard(request):
    bookings = request.user.bookings.all()
    return render(request, 'booking/dashboard.html', {'bookings': bookings})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
