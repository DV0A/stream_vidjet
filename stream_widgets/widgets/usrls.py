from django.urls import path

from . import views

app_mane = 'widgets'

urlpatterns = [
    path('widget/', views.widgets, name='widget'),
]
