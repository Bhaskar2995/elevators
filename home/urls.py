from django.contrib import admin
from django.urls import path
from .views import Index

urlpatterns = [
    path('',Index.as_view()),
    path('initialize/<int:elevators>',Index.as_view()),
    path('maintenance/<int:maintenance>',Index.as_view()),
    path('floor/<int:user_request>',Index.as_view()),
    path('fetch/<int:elevator_status>',Index.as_view()),
    path('request/<int:elevator_request>',Index.as_view()),
    path('next/<int:next_destination>',Index.as_view()),
    path('state/<int:state_elevator>/<str:state>',Index.as_view())
]