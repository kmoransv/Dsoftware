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

@permission_required('auth.Can add permission', login_url='/Acceso/')
def ConsultarClinica(request):
    iTblClinica = TblClinica.objects.all()
    return render_to_response("ConsultarClinica.html",
                              {"iTblClinica":iTblClinica},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def AgregarClinica(request):
    if request.method == "POST":
        iFrmClinica = FrmClinica(request.POST)
        if iFrmClinica.is_valid():
            iFrmClinica.save()
            return HttpResponseRedirect("/Administracion/Consultar/Clinica/")
    else:
        iFrmClinica = FrmClinica()

    return render_to_response("AgregarClinica.html",
                              {"iFrmClinica":iFrmClinica},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EliminarClinica(request, id_clinica):
    clinica = TblClinica.objects.get(pk=id_clinica)
    clinica.delete()
    return HttpResponseRedirect("/Administracion/Clinica/Consultar/")
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EditarClinica(request, id_clinica):
    clinica = TblClinica.objects.get(pk=id_clinica)
    if request.method == "POST":
        iFrmClinica = FrmClinica(request.POST, instance=clinica)
        if iFrmClinica.is_valid():
            iFrmClinica.save()
            return HttpResponseRedirect("/Administracion/Clinica/Consultar/")
    else:
        iFrmClinica = FrmClinica(instance=clinica)

    return render_to_response("EditarClinica.html",
                              {"iFrmClinica":iFrmClinica},
                              context_instance=RequestContext(request))
    
@permission_required('auth.Can add permission', login_url='/Acceso/')
def ConsultarEspecialidad(request):
    iTblEspecialidad = TblEspecialidad.objects.all()
    return render_to_response("ConsultarEspecialidad.html",
                              {"iTblEspecialidad":iTblEspecialidad},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def AgregarEspecialidad(request):
    if request.method == "POST":
        iFrmEspecialidad = FrmEspecialidad(request.POST)
        if iFrmEspecialidad.is_valid():
            iFrmEspecialidad.save()
            return HttpResponseRedirect("/Administracion/Consultar/Especialidad/")
    else:
        iFrmEspecialidad = FrmEspecialidad()

    return render_to_response("AgregarEspecialidad.html",
                              {"iFrmEspecialidad":iFrmEspecialidad},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EliminarEspecialidad(request, id_especialidad):
    especialidad = TblEspecialidad.objects.get(pk=id_especialidad)
    especialidad.delete()
    return HttpResponseRedirect("/Administracion/Consultar/Especialidad/")
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EditarEspecialidad(request, id_especialidad):
    especialidad = TblEspecialidad.objects.get(pk=id_especialidad)
    if request.method == "POST":
        iFrmEspecialidad = FrmEspecialidad(request.POST, instance=especialidad)
        if iFrmEspecialidad.is_valid():
            iFrmEspecialidad.save()
            return HttpResponseRedirect("/Administracion/Consultar/Especialidad/")
    else:
        iFrmEspecialidad = FrmEspecialidad(instance=especialidad)
    return render_to_response("EditarEspecialidad.html",
                              {"iFrmEspecialidad":iFrmEspecialidad},
                              context_instance=RequestContext(request))
    
    @permission_required('auth.Can add permission', login_url='/Acceso/')
def ConsultarEstado(request):
    iTblEstado = TblEstado.objects.all()
    return render_to_response("ConsultarEstado.html",
                              {"iTblEstado":iTblEstado},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def AgregarEstado(request):
    if request.method == "POST":
        iFrmEstado = FrmEstado(request.POST)
        if iFrmEstado.is_valid():
            iFrmEstado.save()
            return HttpResponseRedirect("/Administracion/Consultar/Estado/")
    else:
        iFrmEstado = FrmEstado()
    return render_to_response("AgregarEstado.html",
                              {"iFrmEstado":iFrmEstado},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EditarEstado(request, id_estado):
    estado = TblEstado.objects.get(pk=id_estado)
    if request.method == "POST":
        iFrmEstado = FrmEstado(request.POST, instance=estado)
        if iFrmEstado.is_valid():
            iFrmEstado.save()
            return HttpResponseRedirect("/Administracion/Consultar/Estado/")
    else:
        iFrmEstado = FrmEstado(instance=estado)
    return render_to_response("EditarEstado.html",
                              {"iFrmEstado":iFrmEstado},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EliminarEstado(request, id_estado):
    estado = TblEstado.objects.get(pk=id_estado)
    estado.delete()
    return HttpResponseRedirect("/Administracion/Consultar/Estado/")