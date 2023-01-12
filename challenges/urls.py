from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenge_page, name="challenge_page"), # /challenge/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge"),   
]
