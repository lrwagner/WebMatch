"""urls für pages app, müssen in django_dwh/urls.py eingebunden werden.
"""
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
