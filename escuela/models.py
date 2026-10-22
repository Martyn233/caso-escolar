from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now as ahora

# Usuario extiende el User nativo de Django (AbstractUser), así hereda
# username, password, first_name, last_name, email, is_active, login, permisos, etc.
class Usuario(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('DOCENTE', 'Docente'),
        ('ALUMNO', 'Alumno'),
        ('APODERADO', 'Apoderado'),
    ]
    rol = models.CharField('Rol', max_length=25, choices=ROLES, default='ALUMNO')
    rut = models.CharField('RUT', max_length=12, unique=True, null=True, blank=True)
    telefono = models.CharField('Teléfono', max_length=15, null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Usuarios del sistema escolar (administradores, docentes, alumnos y apoderados)."

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.rol})"

class Alumno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField('Fecha Nacimiento', null=False)
    apoderado = models.CharField('Nombre Apoderado', max_length=100, null=False)
    info_medica = models.TextField('Información Médica', max_length=500, null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Datos académicos y personales de alumnos."

    def __str__(self):
        return str(self.usuario)

class Docente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    especialidad = models.CharField('Especialidad', max_length=100, null=False)
    fecha_contratacion = models.DateField('Fecha Contratación', null=False)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Datos laborales de docentes."

    def __str__(self):
        return f"{self.usuario} - {self.especialidad}"

class PeriodoAcademico(models.Model):
    anio = models.IntegerField('Año', null=False)
    semestre = models.IntegerField('Semestre', null=False)
    activo = models.BooleanField('Periodo Activo', default=True)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Periodos académicos (año y semestre)."
        unique_together = ('anio', 'semestre')

    def __str__(self):
        return f"{self.anio} - S{self.semestre}"

class Asignatura(models.Model):
    codigo = models.CharField('Código Asignatura', max_length=25, unique=True, null=False)
    nombre = models.CharField('Nombre Asignatura', max_length=100, null=False)
    descripcion = models.TextField('Descripción', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Asignaturas impartidas en la escuela."

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Curso(models.Model):
    periodo = models.ForeignKey(PeriodoAcademico, on_delete=models.PROTECT)
    docente_jefe = models.ForeignKey(Docente, on_delete=models.PROTECT)
    nombre = models.CharField('Nombre Curso', max_length=50, null=False)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Cursos de un periodo académico, con su docente jefe."

    def __str__(self):
        return f"{self.nombre} ({self.periodo})"

class Clase(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Asignatura dictada por un docente en un curso específico."

    def __str__(self):
        return f"{self.asignatura.nombre} - {self.curso.nombre}"

class Matricula(models.Model):
    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('RETIRADA', 'Retirada'),
        ('FINALIZADA', 'Finalizada'),
    ]
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    estado = models.CharField('Estado Matrícula', max_length=25, choices=ESTADOS, default='ACTIVA')
    fecha_inscripcion = models.DateField('Fecha Inscripción', null=False)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Inscripción de un alumno en un curso."
        unique_together = ('alumno', 'curso')

    def __str__(self):
        return f"{self.alumno} en {self.curso}"

class Calificacion(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT)
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    nota = models.DecimalField('Nota', max_digits=3, decimal_places=1, null=False)
    ponderacion = models.DecimalField('Ponderación', max_digits=5, decimal_places=2, null=False)
    observacion = models.TextField('Observación', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Notas de alumnos en una clase (escala 1.0 a 7.0)."

    def __str__(self):
        return f"{self.alumno} - {self.clase}: {self.nota}"

class Asistencia(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT)
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    fecha = models.DateField('Fecha Asistencia', null=False)
    presente = models.BooleanField('Presente', default=True)
    justificado = models.BooleanField('Justificado', default=False)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Registro diario de asistencia de alumnos por clase."
        unique_together = ('clase', 'alumno', 'fecha')

    def __str__(self):
        return f"{self.alumno} - {self.fecha} ({'Presente' if self.presente else 'Ausente'})"

class RegistroAuditoria(models.Model):
    usuario_responsable = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    entidad_afectada = models.CharField('Entidad Afectada', max_length=50, null=False)
    id_registro = models.IntegerField('ID Registro', null=False)
    tipo_evento = models.CharField('Tipo de Evento', max_length=25, null=False)
    descripcion = models.TextField('Descripción del Evento', max_length=500, null=False)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    class Meta:
        db_table_comment = "Bitácora de cambios realizados por los usuarios."

    def __str__(self):
        return f"{self.tipo_evento} en {self.entidad_afectada} #{self.id_registro}"
