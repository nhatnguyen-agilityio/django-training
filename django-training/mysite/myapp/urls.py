from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-form', views.get_contact, name='get_contact'),
    path('thanks/', views.move_to_thanks_page, name='move_to_thanks_page'),
]
