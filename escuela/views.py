from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets

from .models import Usuario, Alumno, Docente, PeriodoAcademico, Asignatura, Curso
from .models import Clase, Matricula, Calificacion, Asistencia, RegistroAuditoria

from .serializer import UsuarioSerializer, AlumnoSerializer, DocenteSerializer, PeriodoAcademicoSerializer
from .serializer import AsignaturaSerializer, CursoSerializer, ClaseSerializer, MatriculaSerializer
from .serializer import CalificacionSerializer, AsistenciaSerializer, RegistroAuditoriaSerializer

# Secciones que se muestran en la página de inicio: (titulo, icono, descripcion, modelo, ruta de la API)
SECCIONES = [
    ('Comunidad', [
        ('Usuarios', '👤', 'Cuentas de acceso y roles', Usuario, 'usuarios'),
        ('Alumnos', '🎒', 'Fichas de estudiantes y apoderados', Alumno, 'alumnos'),
        ('Docentes', '👩‍🏫', 'Profesores y especialidades', Docente, 'docentes'),
    ]),
    ('Organización Académica', [
        ('Periodos', '📅', 'Años y semestres académicos', PeriodoAcademico, 'periodos'),
        ('Asignaturas', '📚', 'Ramos que imparte la escuela', Asignatura, 'asignaturas'),
        ('Cursos', '🏫', 'Cursos y su docente jefe', Curso, 'cursos'),
        ('Clases', '🧑‍🏫', 'Asignatura + curso + docente', Clase, 'clases'),
    ]),
    ('Seguimiento', [
        ('Matrículas', '📝', 'Inscripción de alumnos en cursos', Matricula, 'matriculas'),
        ('Calificaciones', '💯', 'Notas de 1.0 a 7.0', Calificacion, 'calificaciones'),
        ('Asistencia', '✅', 'Presentes, ausentes y justificados', Asistencia, 'asistencias'),
    ]),
    ('Sistema', [
        ('Auditoría', '🔍', 'Registro de cambios realizados', RegistroAuditoria, 'auditoria'),
    ]),
]

def bienvenida(request):
    grupos = []
    for titulo_grupo, items in SECCIONES:
        tarjetas = []
        for titulo, icono, descripcion, modelo, ruta_api in items:
            tarjetas.append({
                'titulo': titulo,
                'icono': icono,
                'descripcion': descripcion,
                'cantidad': modelo.objects.count(),
                # nombre de ruta del admin: admin:<app>_<modelo>_changelist
                'url_admin': reverse(f'admin:escuela_{modelo._meta.model_name}_changelist'),
                'url_api': f'/escuela/{ruta_api}/',
            })
        grupos.append({'titulo': titulo_grupo, 'tarjetas': tarjetas})
    return render(request, 'bienvenida.html', {'grupos': grupos})

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class PeriodoAcademicoViewSet(viewsets.ModelViewSet):
    queryset = PeriodoAcademico.objects.all()
    serializer_class = PeriodoAcademicoSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class RegistroAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAuditoria.objects.all()
    serializer_class = RegistroAuditoriaSerializer
