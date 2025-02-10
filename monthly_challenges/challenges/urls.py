from django.urls import path
from . import views

urlpatterns=[
    # path("january", views.january),
    # path("february", views.february)
    path("", view=views.index),
    path("<int:month>", view=views.monthly_challenge_by_number),
    path("<str:month>", view=views.monthly_challenge, name="month-challenge"),
]