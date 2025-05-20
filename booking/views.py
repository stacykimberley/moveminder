from django.shortcuts import render, redirect, get_object_or_404
from .models import GymClass
from .forms import BookingForm
from django.forms import Select

def index(request):
    return render(request, 'booking/index.html')

def home(request):
    return render(request, 'booking/index.html')

def about(request):
    return render(request, 'booking/about.html')

def classes(request):
    classes = GymClass.objects.all()
    return render(request, 'booking/classes.html', {'classes': classes})

""" def book_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)
    return render(request, 'booking/booking_form.html', {'gym_class': gym_class}) """

def book_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.gym_class = gym_class
            booking.save()
            return redirect('booking_success')  # Add a success page view/url
    else:
        form = BookingForm()
        form.fields['time_slot'].widget = Select(choices=[(slot, slot) for slot in gym_class.get_time_slots()])

    return render(request, 'booking/booking_form.html', {
        'gym_class': gym_class,
        'form': form,
    })

def booking_success(request):
    return render(request, 'booking/success.html')
