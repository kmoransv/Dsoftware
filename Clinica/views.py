# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required

from django.core.exceptions import ObjectDoesNotExist

from Clinica.models import *
from Clinica.forms import *
from django.contrib.auth.models import *
from django.utils.formats import date_format

import datetime

def index(request):
    return render_to_response("Clinica.html", context_instance=RequestContext(request))