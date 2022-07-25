from django.urls import path
from .views import HomePageView, LoginPageView
import django.urls 


urlpatterns = [
path("login/", LoginPageView.as_view(), name="login"),
]