from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('extendCard',views.extendCard)
]