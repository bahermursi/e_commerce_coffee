"""
Urls for app
"""
# pylint: disable=ungrouped-imports
from django.urls import path, include
from django.conf.urls import url
from coffee.views.machine import MachineView
from coffee.views.pod import PodView
from rest_framework.routers import DefaultRouter

urlpatterns = [
        path('machines/', MachineView.as_view()),
        path('pods/', PodView.as_view()),
]