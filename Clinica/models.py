from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class TblClinica(models.Model):
    id_clinica = models.AutoField(primary_key=True)
    num_registro = models.CharField(max_length=51)
    nombre_clinica = models.CharField(max_length=150)
    telefono_clinica = models.CharField(max_length=27)
    fax_clinica = models.CharField(max_length=27, blank=True)
    direccion_clinica = models.CharField(max_length=240)
    correo_clinica = models.CharField(max_length=150, blank=True)
    web_clinica = models.CharField(max_length=225)
    class Meta:
        db_table = u'tbl_clinica'

class TblPaciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, unique=True)
    nombre_paciente = models.CharField(max_length=75)
    apellido_paciente = models.CharField(max_length=75)
    genero_paciente = models.CharField(max_length=1, choices=GENERO)
    fecha_nacimiento_paciente = models.DateField()
    estatura_paciente = models.DecimalField(null=True, max_digits=11, decimal_places=0, blank=True)
    dui_paciente = models.CharField(max_length=30)
    telefono_paciente = models.CharField(max_length=27)
    direccion_paciente = models.CharField(max_length=240)
    class Meta:
        db_table = u'tbl_paciente'

class TblEmpleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, unique=True)
    id_clinica = models.ForeignKey(TblClinica, db_column='id_clinica')
    nombre_empleado = models.CharField(max_length=75)
    apellido_empleado = models.CharField(max_length=75)
    genero_empleado = models.CharField(max_length=1, choices=GENERO)
    fecha_nacimiento_empleado = models.DateField()
    telefono_empleado = models.CharField(max_length=27)
    dui_empleado = models.CharField(max_length=30)
    direccion_empleado = models.CharField(max_length=240)
    class Meta:
        db_table = u'tbl_empleado'

class TblMedico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, unique=True)
    id_clinica = models.ForeignKey(TblClinica, db_column='id_clinica')
    nombre_medico = models.CharField(max_length=75)
    apellido_medico = models.CharField(max_length=75)
    genero_medico = models.CharField(max_length=1, choices=GENERO)
    fecha_nacimiento_medico = models.DateField()
    telefono_medico = models.CharField(max_length=27)
    dui_medico = models.CharField(max_length=30)
    direccion_medico = models.CharField(max_length=240)
    class Meta:
        db_table = u'tbl_medico'

class TblCatalogoExpediente(models.Model):
    id_catalogo = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(TblPaciente, db_column='id_paciente')
    id_medico = models.ForeignKey(TblMedico, db_column='id_medico')
    class Meta:
        db_table = u'tbl_catalogo_expediente'

class TblEstado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion_estado = models.CharField(max_length=45)
    class Meta:
        db_table = u'tbl_estado'

class TblCita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(TblPaciente, db_column='id_paciente')
    id_medico = models.ForeignKey(TblMedico, db_column='id_medico')
    id_estado = models.ForeignKey(TblEstado, db_column='id_estado')
    fecha_realizada = models.DateTimeField(auto_now=True)
    fecha_solicitada = models.DateField()
    hora_solicitada = models.TimeField()
    class Meta:
        db_table = u'tbl_cita'

class TblDetalleExpediente(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_catalogo = models.ForeignKey(TblCatalogoExpediente, db_column='id_catalogo')
    id_medico = models.ForeignKey(TblMedico, db_column='id_medico')
    id_cita = models.ForeignKey(TblCita, db_column='id_cita')
    diagnostico = models.CharField(max_length=3000)
    tratamiento = models.CharField(max_length=3000)
    peso = models.DecimalField(max_digits=11, decimal_places=2)
    fecha = models.DateField()
    class Meta:
        db_table = u'tbl_detalle_expediente'

class TblEspecialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    descripcion_especialidad = models.CharField(max_length=150)
    class Meta:
        db_table = u'tbl_especialidad'

class TblEspecialidadXMedico(models.Model):
    id_especialidad_x_medico = models.AutoField(primary_key=True)
    id_especialidad = models.ForeignKey(TblEspecialidad, db_column='id_especialidad')
    id_medico = models.ForeignKey(TblMedico, db_column='id_medico')
    class Meta:
        db_table = u'tbl_especialidad_x_medico'

class TblHorario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    id_medico = models.ForeignKey(TblMedico, db_column='id_medico')
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    class Meta:
        db_table = u'tbl_horario'