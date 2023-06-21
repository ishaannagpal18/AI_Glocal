from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
import uuid
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import *
from django.core.mail import send_mail
from django.views import View


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')