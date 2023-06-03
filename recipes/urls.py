from django.urls import path

from .views import home, recipe

urlpatterns = [
    path('', home),
    path('recipes/<int:id>/', recipe),
]
