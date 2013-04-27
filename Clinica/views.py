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
    return HttpResponseRedirect("/Administracion/Consultar/Clinica/")
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EditarClinica(request, id_clinica):
    clinica = TblClinica.objects.get(pk=id_clinica)
    if request.method == "POST":
        iFrmClinica = FrmClinica(request.POST, instance=clinica)
        if iFrmClinica.is_valid():
            iFrmClinica.save()
            return HttpResponseRedirect("/Administracion/Consultar/Clinica/")
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

@permission_required('auth.Can add permission', login_url='/Acceso/')
def ConsultarMedico(request):
    iTblMedico = TblMedico.objects.all()
    return render_to_response("ConsultarMedico.html",
                              {"iTblMedico":iTblMedico},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EliminarMedico(request, id_medico):
    medico = TblMedico.objects.get(pk=id_medico)
    usuario = User.objects.get(username = medico.dui_medico)
    medico.delete()
    usuario.delete()
    return HttpResponseRedirect("/Usuarios/Consultar/Medicos/")
@permission_required('auth.Can add permission', login_url='/Acceso/')
def AgregarMedico(request):
    if request.method == "POST":
        iFrmMedico = FrmMedico(request.POST)
        if iFrmMedico.is_valid():
            U = User.objects.create_user(request.POST['dui_medico'],
                                         'notiene@notiene.com',
                                         request.POST['Contrasena'])
            U.save()
            idU = User.objects.latest('id')
            '''idG = Group.objects.get(pk=2)
            idG.user_set.add(idU)'''

            UStaff = User.objects.latest('id')
            UStaff.is_staff = 1
            UStaff.save()

            uMedico = User.objects.latest('id')
            permiso = Permission.objects.get(name='Can add tbl catalogo expediente')
            uMedico.user_permissions.add(permiso)

            idC = TblClinica.objects.get(pk=1)
            NiFrmMedico = iFrmMedico.save(commit=False)
            NiFrmMedico.user = idU
            NiFrmMedico.id_clinica = idC
            NiFrmMedico.save()

            iTblMedico = TblMedico.objects.latest('id_medico')
            iTblHorario = TblHorario(id_medico=iTblMedico,
                                     hora_entrada='07:00',
                                     hora_salida='18:00')
            iTblHorario.save()

            return HttpResponseRedirect("/index/Administracion")

    else:
        iFrmMedico = FrmMedico()
    return render_to_response("AgregarMedico.html",
                              {"iFrmMedico":iFrmMedico},
                              context_instance=RequestContext(request))

@permission_required('Clinica.add_tblcatalogoexpediente', login_url='/Acceso/')
def ConsultarHorario(request):
    iTblMedico = TblMedico.objects.get(dui_medico=request.user.username)
    #iTblHorario = TblHorario.objects.get(id_medico=int(iTblMedico.id_medico))
    consulta = "SELECT t1.id_horario, t2.nombre_medico, t2.apellido_medico, t1.hora_entrada, t1.hora_salida FROM tbl_horario AS t1 INNER JOIN tbl_medico AS t2 ON t1.id_medico = t2.id_medico WHERE t1.id_medico = %d;" %int(iTblMedico.id_medico)
    iTblHorario = TblHorario.objects.raw(consulta)
    return render_to_response("ConsultarHorario.html",
                              {"iTblHorario":iTblHorario},
                              context_instance=RequestContext(request))

@permission_required('Clinica.add_tblcatalogoexpediente', login_url='/Acceso/')
def EditarHorario(request, id_horario):
    horario = TblHorario.objects.get(pk=id_horario)
    if request.method == "POST":
        iFrmHorario = FrmHorario(request.POST, instance=horario)
        if iFrmHorario.is_valid():
            #iFrmHorario.save()
            hora_entrada = datetime.datetime.strptime(request.POST['hora_entrada'], '%I:%M %p').strftime('%H:%M')
            hora_salida = datetime.datetime.strptime(request.POST['hora_salida'], '%I:%M %p').strftime('%H:%M')
            medico = TblMedico.objects.get(dui_medico=request.user.username)
            iTblHorario = TblHorario.objects.get(id_medico=medico.id_medico)
            iTblHorario.hora_entrada = hora_entrada
            iTblHorario.hora_salida = hora_salida
            iTblHorario.save()
            return HttpResponseRedirect("/Usuarios/Medico/Horario/Consultar/")
    else:
        iFrmHorario = FrmHorario()
    return render_to_response("EditarHorario.html",
                              {"iFrmHorario":iFrmHorario},
                              context_instance=RequestContext(request))

@permission_required('auth.Can add permission', login_url='/Acceso/')
def MedicoEspecialidad(request):
    if request.method == "POST":
        iFrmMedicoE = FrmMedicoE(request.POST)
        if iFrmMedicoE.is_valid():
            try:
                medico = TblMedico.objects.get(dui_medico=request.POST['Documento'])
                return HttpResponseRedirect("/Usuarios/Medico/Especialidad/Especialidades/%d" %medico.id_medico)
            except ObjectDoesNotExist, e:
                return HttpResponse("El Medico no Existe")
    else:
        iFrmMedicoE = FrmMedicoE()
    return render_to_response("MedicoE.html",
                              {"iFrmMedicoE":iFrmMedicoE},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EspecialidadxMedico(request, id_medico):
    iTblEspecialidad = TblEspecialidad.objects.all()
    iTblMedico = TblMedico.objects.get(id_medico=id_medico)
    consulta = "SELECT t1.id_especialidad, t1.descripcion_especialidad FROM tbl_especialidad AS t1 INNER JOIN tbl_especialidad_x_medico AS t2 ON t1.id_especialidad = t2.id_especialidad WHERE t2.id_medico = %d" %int(id_medico)
    Especialidad = TblEspecialidad.objects.raw(consulta)
    return render_to_response("EspecialidadMedico.html",
                              {"iTblEspecialidad":iTblEspecialidad,
                               "iTblMedico":iTblMedico,
                               "iTblEspecialidadxMedico":Especialidad},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EspecialidadxMedicoAgregar(request, id_especialidad, id_medico):
    medico = TblMedico.objects.get(pk=id_medico)
    especialidad = TblEspecialidad.objects.get(pk=id_especialidad)
    try:
        especialidadxmedico = TblEspecialidadXMedico.objects.get(id_medico=medico, id_especialidad=especialidad)
        return HttpResponseRedirect("/Usuarios/Medico/Especialidad/Especialidades/%d" %int(id_medico))
    except ObjectDoesNotExist, e:
        especialidadxmedico = TblEspecialidadXMedico(id_especialidad=especialidad, id_medico=medico)
        especialidadxmedico.save()
        return HttpResponseRedirect("/Usuarios/Medico/Especialidad/Especialidades/%d" %int(id_medico))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EspecialidadxMedicoEliminar(requese, id_especialidad, id_medico):
    especialidadxmedico = TblEspecialidadXMedico.objects.get(id_especialidad=int(id_especialidad), id_medico=int(id_medico))
    especialidadxmedico.delete()
    return HttpResponseRedirect("/Usuarios/Medico/Especialidad/Especialidades/%d" %int(id_medico))

@permission_required('auth.Can add permission', login_url='/Acceso/')
def ConsultarEmpleado(request):
    iTblEmpleado = TblEmpleado.objects.all()
    return render_to_response("ConsultarEmpleado.html",
                              {"iTblEmpleado":iTblEmpleado},
                              context_instance=RequestContext(request))
@permission_required('auth.Can add permission', login_url='/Acceso/')
def EliminarEmpleado(request, id_empleado):
    empleado = TblEmpleado.objects.get(pk=id_empleado)
    usuario = User.objects.get(username = empleado.dui_empleado)
    empleado.delete()
    usuario.delete()
    return HttpResponseRedirect("/Usuarios/Consultar/Empleados/")
@permission_required('auth.Can add permission', login_url='/Acceso/')
def AgregarEmpleado(request):
    if request.method == "POST":
        iFrmEmpleado = FrmEmpleado(request.POST)
        if iFrmEmpleado.is_valid():
            U = User.objects.create_user(request.POST['dui_empleado'],
                                         'notiene@notiene.com',
                                         request.POST['Contrasena'])
            U.save()
            idU = User.objects.latest('id')
            '''idG = Group.objects.get(pk=2)
            idG.user_set.add(idU)'''

            uEmpleado = User.objects.latest('id')
            permiso = Permission.objects.get(name='Can add tbl cita')
            uEmpleado.user_permissions.add(permiso)

            UStaff = User.objects.latest('id')
            UStaff.is_staff = 1
            UStaff.save()
            idC = TblClinica.objects.get(pk=1)
            NiFrmEmpleado = iFrmEmpleado.save(commit=False)
            NiFrmEmpleado.user = idU
            NiFrmEmpleado.id_clinica = idC
            NiFrmEmpleado.save()
            return HttpResponseRedirect("/index/Administracion")

    else:
        iFrmEmpleado = FrmEmpleado()
    return render_to_response("AgregarEmpleado.html",
                              {"iFrmEmpleado":iFrmEmpleado},
                              context_instance=RequestContext(request))
    
@login_required(login_url='/Acceso/')
def ConsultarCita(request):
    consulta = "SELECT t1.id_cita, t3.nombre_medico, t3.apellido_medico, t1.fecha_solicitada, t1.hora_solicitada FROM tbl_cita AS t1 INNER JOIN tbl_paciente AS t2 ON t1.id_paciente = t2.id_paciente INNER JOIN tbl_medico AS t3 ON t1.id_medico = t3.id_medico WHERE t2.dui_paciente = '%s' ORDER BY t1.fecha_solicitada;" %request.user.username
    iTblCita = TblCita.objects.raw(consulta)
    return render_to_response("ConsultarCita.html",
                              {"iTblCita":iTblCita},
                              context_instance=RequestContext(request))

@login_required(login_url='/Acceso/')
def CitaPaciente(request):
    paciente = TblPaciente.objects.get(dui_paciente=request.user.username)
    if request.method == "POST":
        iFrmCitaPaciente = FrmCitaPaciente(request.POST)
        return HttpResponseRedirect("/Usuario/Paciente/Cita/Agregar/%d/%d/" %(int(paciente.id_paciente),
                                                                              int(request.POST['Especialidad'])))
    else:
        iFrmCitaPaciente = FrmCitaPaciente()
    return render_to_response("CitaPaciente.html",
                              {"iFrmCitaPaciente":iFrmCitaPaciente},
                              context_instance=RequestContext(request))

@permission_required('Clinica.add_tblcatalogoexpediente', login_url='/Acceso/')
def CitaPaciente2(request):
    if request.method == "POST":
        iFrmCitaPaciente2 = FrmCitaPaciente2(request.POST)
        paciente = TblPaciente.objects.get(dui_paciente=request.POST['Documento_Paciente'])
        return HttpResponseRedirect("/Usuario/Paciente/Cita/Agregar/%d/%d/" %(int(paciente.id_paciente),
                                                                              int(request.POST['Especialidad'])))
    else:
        iFrmCitaPaciente2 = FrmCitaPaciente2()
    return render_to_response("CitaPaciente2.html",
                              {"iFrmCitaPaciente2":iFrmCitaPaciente2},
                              context_instance=RequestContext(request))
    
@login_required(login_url='/Acceso/')
def AgregarCita(request, id_paciente, id_especialidad):
    iTblMedico = TblMedico.objects.raw("SELECT t1.id_medico, t1.nombre_medico, t1.apellido_medico FROM tbl_medico AS t1 INNER JOIN tbl_especialidad_x_medico AS t2 ON t1.id_medico = t2.id_medico WHERE id_especialidad = %d;" %int(id_especialidad))
    if request.method == "POST":
        fecha = datetime.datetime.strptime(request.POST['fecha_cita'], '%d/%m/%Y').strftime('%Y-%m-%d')
        hora = datetime.datetime.strptime(request.POST['hora_cita'], '%I:%M %p').strftime('%H:%M')
        iTblEstado = TblEstado.objects.get(id_estado=1)
        medico = TblMedico.objects.get(id_medico=request.POST['medico'])
        paciente = TblPaciente.objects.get(id_paciente=id_paciente)
        iTblCita = TblCita(id_paciente=paciente,
                           id_medico=medico,
                           id_estado=iTblEstado,
                           fecha_solicitada=fecha,
                           hora_solicitada=hora)
        iTblCita.save()
        return HttpResponseRedirect("/index/Administracion/")
        #return HttpResponseRedirect("/index/")
    return render_to_response("AgregarCita.html",
                              {"iTblMedico":iTblMedico},
                              context_instance=RequestContext(request))

@permission_required('Clinica.add_tblcatalogoexpediente', login_url='/Acceso/')
def ExpedientePaciente(request):
    if request.method == "POST":
        iFrmExpedientePaciente = FrmExpedientePaciente(request.POST)
        paciente = TblPaciente.objects.get(dui_paciente=request.POST['Documento_Paciente'])
        return HttpResponseRedirect("/Usuarios/Medico/Expediente/Paciente/Cita/%d/" %(int(paciente.id_paciente)))
    else:
        iFrmExpedientePaciente = FrmExpedientePaciente()
    return render_to_response("ExpedientePaciente.html",
                              {"iFrmExpedientePaciente":iFrmExpedientePaciente},
                              context_instance=RequestContext(request))
    #return HttpResponse("Documento del Paciente")
@permission_required('Clinica.add_tblcatalogoexpediente', login_url='/Acceso/')
def ExpedienteCita(request, id_paciente):
    medico = TblMedico.objects.get(dui_medico=request.user.username)
    consulta = "SELECT t1.id_cita, t1.id_paciente, t2.nombre_paciente, t2.apellido_paciente, t1.fecha_solicitada, t1.hora_solicitada FROM tbl_cita AS t1 INNER JOIN tbl_paciente AS t2 ON t1.id_paciente = t2.id_paciente INNER JOIN tbl_medico AS t3 ON t1.id_medico = t3.id_medico WHERE t1.id_paciente = %d AND t1.id_medico = %d ORDER BY t1.fecha_solicitada;" %(int(id_paciente), int(medico.id_medico))
    iTblCita = TblCita.objects.raw(consulta)
    return render_to_response("ConsultarCitaExpediente.html",
                              {"iTblCita":iTblCita},
                              context_instance=RequestContext(request))
    return HttpResponse("Cita del Paciente")
@permission_required('Clinica.add_tblcatalogoexpediente', login_url='/Acceso/')
def ExpedienteClinico(request, id_cita):
     iFrmExpediente = FrmExpediente()
     return render_to_response("Expediente.html",{"iFrmExpediente":iFrmExpediente},context_instance=RequestContext(request))
    #return HttpResponse("Expediente Clinico")