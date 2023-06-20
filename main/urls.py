from django.urls import include, path
from main import views

# app_name = 'home'
urlpatterns = [
    # The home page
    path('', views.Home.as_view(), name='home'),
]