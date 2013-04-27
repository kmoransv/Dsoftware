from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Dsoftware.views.home', name='home'),
    # url(r'^Dsoftware/', include('Dsoftware.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

     url(r'^$', 'Clinica.views.index'),
     url(r'^index/Administracion/$','Clinica.views.indexP'),
     url(r'Cerrar/','Clinica.views.Cerrar'),

     #Tbl_Clinica
     url(r'^Administracion/Consultar/Clinica/$','Clinica.views.ConsultarClinica'),
     url(r'^Administracion/Agregar/Clinica/$','Clinica.views.AgregarClinica'),
     url(r'^Administracion/Eliminar/Clinica/(?P<id_clinica>\d+)$','Clinica.views.EliminarClinica'),
     url(r'^Administracion/Editar/Clinica/(?P<id_clinica>\d+)$','Clinica.views.EditarClinica'),

     url(r'^Administracion/Consultar/Especialidad/$','Clinica.views.ConsultarEspecialidad'),
     url(r'^Administracion/Agregar/Especialidad/$','Clinica.views.AgregarEspecialidad'),
     url(r'^Administracion/Eliminar/Especialidad/(?P<id_especialidad>\d+)$','Clinica.views.EliminarEspecialidad'),
     url(r'^Administracion/Editar/Especialidad/(?P<id_especialidad>\d+)$','Clinica.views.EditarEspecialidad'),

     url(r'^Administracion/Consultar/Estado/$','Clinica.views.ConsultarEstado'),
     url(r'^Administracion/Agregar/Estado/$','Clinica.views.AgregarEstado'),
     url(r'^Administracion/Eliminar/Estado/(?P<id_estado>\d+)$','Clinica.views.EliminarEstado'),
     url(r'^Administracion/Editar/Estado/(?P<id_estado>\d+)$','Clinica.views.EditarEstado'),

     #Accesos
     url(r'^Acceso/$', 'Clinica.views.Acceso'),
     #url(r'^Error/$', 'Clinica.views.Error'),

     #Agregar Usuarios
     url(r'^Usuarios/Agregar/Pacientes/$', 'Clinica.views.AgregarPaciente'),
     url(r'^Usuarios/Consultar/Pacientes/$', 'Clinica.views.ConsultarPaciente'),
     url(r'^Usuarios/Eliminar/Pacientes/(?P<id_paciente>\d+)/$', 'Clinica.views.EliminarPaciente'),

     url(r'^Usuarios/Consultar/Empleados/$', 'Clinica.views.ConsultarEmpleado'),
     url(r'^Usuarios/Eliminar/Empleados/(?P<id_empleado>\d+)/$', 'Clinica.views.EliminarEmpleado'),
     url(r'^Usuarios/Agregar/Empleados/$', 'Clinica.views.AgregarEmpleado'),

     url(r'^Usuarios/Consultar/Medicos/$', 'Clinica.views.ConsultarMedico'),
     url(r'^Usuarios/Eliminar/Medicos/(?P<id_medico>\d+)/$', 'Clinica.views.EliminarMedico'),
     url(r'^Usuarios/Agregar/Medicos/$', 'Clinica.views.AgregarMedico'),

     url(r'^Usuarios/Medico/Especialidad$', 'Clinica.views.MedicoEspecialidad'),
     url(r'^Usuarios/Medico/Especialidad/Especialidades/(?P<id_medico>\d+)/$', 'Clinica.views.EspecialidadxMedico'),
     url(r'^Usuarios/Medico/Especialidad/Especialidades/Agregar/(?P<id_especialidad>\d+)/(?P<id_medico>\d+)/$', 'Clinica.views.EspecialidadxMedicoAgregar'),
     url(r'^Usuarios/Medico/Especialidad/Especialidades/Eliminar/(?P<id_especialidad>\d+)/(?P<id_medico>\d+)/$', 'Clinica.views.EspecialidadxMedicoEliminar'),

     url(r'^Usuarios/Medico/Horario/Consultar/$', 'Clinica.views.ConsultarHorario'),
     url(r'^Usuarios/Medico/Horario/Editar/(?P<id_horario>\d+)$', 'Clinica.views.EditarHorario'),
     #url(r'^Usuarios/Medico/Horario/Agregar/$', 'Clinica.views.AgregarHorario'),

     url(r'^Usuarios/Medico/Expediente/Paciente/Documento/$', 'Clinica.views.ExpedientePaciente'),
     url(r'^Usuarios/Medico/Expediente/Paciente/Cita/(?P<id_paciente>\d+)/$', 'Clinica.views.ExpedienteCita'),
     #url(r'^Usuarios/Medico/Expediente/Paciente/(?P<id_paciente>\d+)/(?P<id_cita>\d+)/$', 'Clinica.views.ExpedienteClinico'),
     url(r'^Usuarios/Medico/Expediente/Paciente/(?P<id_cita>\d+)/$', 'Clinica.views.ExpedienteClinico'),

     url(r'^Usuario/Paciente/Cita/Consultar/$', 'Clinica.views.ConsultarCita'),
     url(r'^Usuario/Paciente/Cita/$', 'Clinica.views.CitaPaciente'),
     url(r'^Usuario/Paciente/Cita2/$', 'Clinica.views.CitaPaciente2'),
     url(r'^Usuario/Paciente/Cita/Agregar/(?P<id_paciente>\d+)/(?P<id_especialidad>\d+)/$', 'Clinica.views.AgregarCita'),

     #url(r'^Usuarios/Medico/Especialidades/(?P<especialidad>\d+)$', 'Clinica.views.EXP'),
     #url(r'^Usuarios/Medico/Especialidades2/(?P<especialidad>\d+)/(?P<medico>\d+)/$', 'Clinica.views.EspecialidadMedico'),


     #url(r'^Usuarios/Agregar/AsistenteAdmon/$', 'Clinica.views.AgregarAsistenteAdmon'),
)

