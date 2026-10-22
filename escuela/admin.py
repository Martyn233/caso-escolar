from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .models import Alumno
from .models import Docente
from .models import PeriodoAcademico
from .models import Asignatura
from .models import Curso
from .models import Clase
from .models import Matricula
from .models import Calificacion
from .models import Asistencia
from .models import RegistroAuditoria

# UserAdmin muestra correctamente los campos heredados de AbstractUser,
# y aquí se agregan los campos propios del sistema escolar.
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Datos Escolares', {'fields': ('rol', 'rut', 'telefono')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos Escolares', {'fields': ('rol', 'rut', 'telefono')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'rol', 'rut', 'is_active')

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(PeriodoAcademico)
admin.site.register(Asignatura)
admin.site.register(Curso)
admin.site.register(Clase)
admin.site.register(Matricula)
admin.site.register(Calificacion)
admin.site.register(Asistencia)
admin.site.register(RegistroAuditoria)
