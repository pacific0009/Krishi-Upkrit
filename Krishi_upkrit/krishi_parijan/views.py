from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    from .controller import Controller
    CONTROLLER = Controller("/dev/cu.usbmodem14131")
    CONTROLLER.run()
    return HttpResponse(html)