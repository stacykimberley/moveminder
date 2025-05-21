from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, gym_class=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.gym_class = gym_class
    
    def clean(self):
        cleaned_data = super().clean()
        if not self.gym_class:
            raise ValidationError("Gym class must be set for booking.")
        # temporarily assign gym_class so model validation passes
        self.instance.gym_class = self.gym_class
        return cleaned_data