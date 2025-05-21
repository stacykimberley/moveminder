from django.contrib.auth.decorators import login_required
from django.forms import Select
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from .models import GymClass
from .forms import BookingForm  # assumes BookingForm is updated to accept gym_class

def index(request):
    return render(request, 'booking/index.html')

def about(request):
    return render(request, 'booking/about.html')

def classes(request):
    all_classes = GymClass.objects.all()
    return render(request, 'booking/classes.html', {'classes': all_classes})

def booking_success(request):
    return render(request, 'booking/success.html')

@login_required
def book_class(request, class_id):
    gym_class = get_object_or_404(GymClass, id=class_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, gym_class=gym_class)  # ✅ Pass gym_class to form
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.gym_class = gym_class
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm(gym_class=gym_class)  # ✅ Pass gym_class to form
        form.fields['time_slot'].widget = Select(
            choices=[(slot, slot) for slot in gym_class.get_time_slots()]
        )

    return render(request, 'booking/booking_form.html', {
        'gym_class': gym_class,
        'form': form,
    })
