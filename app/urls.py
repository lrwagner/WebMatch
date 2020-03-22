"""urls für pages app, müssen in django_dwh/urls.py eingebunden werden.
"""
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('usercreation', views.user_creation_view, name='usercreation'),
    path('user_signup', views.user_signup_view, name='user_signup')
]