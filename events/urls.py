from django.urls import path
from .views import HomePageView, LoginPageView, EventListView
from . import views
import django.urls 


urlpatterns = [
path("", EventListView.as_view(), name="home"),
path("login/", LoginPageView.as_view(), name="login"),
path("events", views.event, name="list-events"),
]