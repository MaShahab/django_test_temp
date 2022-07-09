from django.contrib import admin
from django.urls import path, include
from resume_app.views import index


urlpatterns = [
    path('', index, name= 'index_resume'),
]
