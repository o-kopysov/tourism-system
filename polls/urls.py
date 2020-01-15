from django.urls import path

from .views import

urlpatterns = [
    path('', views.new_home, name='home'),
]
