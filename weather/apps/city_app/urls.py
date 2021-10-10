from django.urls import path

from apps.city_app import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='Home')
]
