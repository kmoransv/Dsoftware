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
def Acceso(request):
    if request.method == "POST":
        iFrmAcceso = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/index/Administracion/")
            else:
                return HttpResponse("Verifica si tu Usuario esta Activo")
        else:
            return HttpResponse("Usuario no Existe")

    else:
        iFrmAcceso = AuthenticationForm()
    return render_to_response("AccesoWeb.html", {'iFrmAcceso':iFrmAcceso}, context_instance=RequestContext(request))
@login_required(login_url='/Acceso/')
def Cerrar(request):
    logout(request)
    return HttpResponseRedirect("/")