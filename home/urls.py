from django.contrib import admin
from django.urls import path
from .views import Index

urlpatterns = [
    path('',Index.as_view()),
    path('initialize/<int:elevators>',Index.as_view())
]