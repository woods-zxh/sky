from . import views
from django.urls import path

urlpatterns =[
    path('', views.recruit, name='recruit')
]