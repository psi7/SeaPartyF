from django.http import (
    Http404,
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpRequest,
)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Events, Location, Category, SubCategory, Users
from django.http import HttpResponse
from django import forms
from django.urls import reverse
import logging
import traceback

logger = logging.getLogger(__name__)
# Create your views here.
class HomePageView(TemplateView):
    template_name = "homepage.html"

class LoginPageView(TemplateView):
    template_name: str= "login.html"

class EventListView(ListView):
    model=Events
    template_name = 'homepage.html'

def index(request):
    logger.debug("Homepage method is called")
    logger.info("Method that loads main page")
    logger.error("Error")
    return render(request, "events/homepage.html", {"events": Events.objects.all()})

def event(request):
    event_list = Events.objects.all()  # get me the events

    return render(
        request,
        "event_list.html",
        {
            "event_list": event_list,
        },
    )