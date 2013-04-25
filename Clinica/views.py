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

@login_required(login_url='/Acceso/')
def indexP(request):
    return render_to_response("ClinicaP.html", context_instance=RequestContext(request))

@permission_required('auth.Can add permission', login_url='/Acceso/')
def Registros(request):
    return HttpResponse("Registros")

def AgregarPaciente(request):
    if request.method == 'POST':
        iFrmPaciente = FrmPaciente(request.POST)
        if iFrmPaciente.is_valid():
            try:
                U = User.objects.create_user(request.POST['dui_paciente'],
                                             'notiene@notiene.com',
                                             request.POST['apellido_paciente'])
                U.save()
                idU = User.objects.latest('id')
                '''idG = Group.objects.get(pk=3)
                idG.user_set.add(idU)'''

                uPaciente = User.objects.latest('id')
                permiso = Permission.objects.get(name='Can add tbl paciente')
                uPaciente.user_permissions.add(permiso)

                NiFrmPaciente = iFrmPaciente.save(commit=False)
                NiFrmPaciente.user = idU
                NiFrmPaciente.save()
                return HttpResponseRedirect("/Acceso/")
            except Exception as e:
                return HttpResponse("usuario ya existe")

    else:
        iFrmPaciente = FrmPaciente()
    return render_to_response("AgregarPaciente.html",
                              {"iFrmPaciente":iFrmPaciente},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def ConsultarPaciente(request):
    iTblPaciente = TblPaciente.objects.all()
    return render_to_response("ConsultarPaciente.html",
                              {"iTblPaciente":iTblPaciente},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EliminarPaciente(request, id_paciente):
    paciente = TblPaciente.objects.get(pk=id_paciente)
    usuario = User.objects.get(username = id.dui_paciente)
    paciente.delete()
    usuario.delete()
    return HttpResponseRedirect("/Usuarios/Consultar/Pacientes/")