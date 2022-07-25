from django.urls import path
from .views import SignUpView
import django.urls 

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]