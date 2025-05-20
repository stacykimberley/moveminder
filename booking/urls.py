from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('book/<int:class_id>/', views.book_class, name='book_class'),
    path('booking/success/', views.booking_success, name='booking_success'),
]

