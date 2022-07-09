from django.contrib import admin
from django.urls import path, include
from main_app.views import index,about,contact, portfolio,services,portfolio,team,blog


urlpatterns = [
    path('', index, name= 'index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('team/', team, name='team'),
    path('blog/', blog, name='blog')
]
