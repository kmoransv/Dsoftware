'''from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import FilteredSelectMultiple'''

#from django.contrib import admin

from django import forms
from Clinica.models import *

class FrmClinica(forms.ModelForm):
    class Meta:
        model = TblClinica
        
class FrmPaciente(forms.ModelForm):
    class Meta:
        model = TblPaciente
        exclude = ('user_id')
        
class FrmEspecialidad(forms.ModelForm):
    class Meta:
        model = TblEspecialidad
        exclude = ('id_especialidad')
        
class FrmEstado(forms.ModelForm):
    class Meta:
        model = TblEstado
        exclude = ('id_estado')

class FrmAcceso(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        
class FrmEmpleado(forms.ModelForm):
    Contrasena = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = TblEmpleado
        fields = ('nombre_empleado',
                  'apellido_empleado',
                  'genero_empleado',
                  'fecha_nacimiento_empleado',
                  'dui_empleado',
                  'telefono_empleado',
                  'direccion_empleado'
                  )
        
class FrmMedico(forms.ModelForm):
    Contrasena = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = TblMedico
        fields = ('nombre_medico',
                  'apellido_medico',
                  'genero_medico',
                  'fecha_nacimiento_medico',
                  'dui_medico',
                  'telefono_medico',
                  'direccion_medico'
                  )

class FrmHorario(forms.ModelForm):
    hora_entrada = forms.CharField(widget=forms.TextInput(attrs={'data-format':'HH:mm PP'}))
    hora_salida = forms.CharField(widget=forms.TextInput(attrs={'data-format':'HH:mm PP'}))
    class Meta:
        model = TblHorario
        fields = ('hora_entrada',
                  'hora_salida')
        
class FrmMedicoE(forms.Form):
    Documento = forms.CharField()
    
class FrmEspecialidadxMedico(forms.ModelForm):
    class Meta:
        model = TblEspecialidadXMedico
        exclude = ('id_especialidad_x_medico')


class EspecialidadModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" %obj.descripcion_especialidad

class MedicoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" %(obj.nombre_medico, obj.apellido_medico)

#.values_list('descripcion_especialidad')
class FrmCitaPaciente(forms.Form):
    Especialidad = EspecialidadModelChoiceField(queryset=TblEspecialidad.objects.all(),
                                          empty_label="Seleccione una Especialidad")

class FrmCitaPaciente2(forms.Form):
    Documento_Paciente = forms.CharField()
    Especialidad = EspecialidadModelChoiceField(queryset=TblEspecialidad.objects.all(),
                                          empty_label="Seleccione una Especialidad")

class FrmExpedientePaciente(forms.Form):
    Documento_Paciente = forms.CharField()

class FrmAgregarCita(forms.Form):
    consulta = ""
    Especialidad = MedicoModelChoiceField(queryset=consulta,
                                          empty_label="Seleccione una Especialidad")


class FrmExpediente(forms.Form):
    #Diagnostico = forms.CharField(max_length=200)
    Diagnostico = forms.CharField(widget=forms.Textarea)
    Tratamiento = forms.CharField(widget=forms.Textarea)
