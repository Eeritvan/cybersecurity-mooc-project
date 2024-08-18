from django.urls import path

from .views import homePageView, addNote, userData

urlpatterns = [
    path('', homePageView, name='home'),
    path('add/', addNote, name='add'),
    path('user/<int:id>/', userData, name='userData'),
]
