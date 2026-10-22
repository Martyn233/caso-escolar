from django.urls import path,include
from rest_framework import routers
from escuela import views

enrutador = routers.DefaultRouter()

enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'alumnos', views.AlumnoViewSet)
enrutador.register(r'docentes', views.DocenteViewSet)
enrutador.register(r'periodos', views.PeriodoAcademicoViewSet)
enrutador.register(r'asignaturas', views.AsignaturaViewSet)
enrutador.register(r'cursos', views.CursoViewSet)
enrutador.register(r'clases', views.ClaseViewSet)
enrutador.register(r'matriculas', views.MatriculaViewSet)
enrutador.register(r'calificaciones', views.CalificacionViewSet)
enrutador.register(r'asistencias', views.AsistenciaViewSet)
enrutador.register(r'auditoria', views.RegistroAuditoriaViewSet)

urlpatterns = [
    path('', include(enrutador.urls))
]
