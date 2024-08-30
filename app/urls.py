from django.urls import path
from .views import *

urlpatterns = [
    path('statuses/', VehicleStatusSummary.as_view()),
]
