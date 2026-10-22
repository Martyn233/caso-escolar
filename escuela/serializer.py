from rest_framework import serializers
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

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # No se expone la contraseña ni los permisos internos de Django
        fields = ('id','username','first_name','last_name','email','rol','rut','telefono','is_active')

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id','usuario','fecha_nacimiento','apoderado','info_medica')

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('id','usuario','especialidad','fecha_contratacion')

class PeriodoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = ('id','anio','semestre','activo')

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id','codigo','nombre','descripcion')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id','nombre','periodo','docente_jefe')

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ('id','curso','asignatura','docente')

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ('id','alumno','curso','estado','fecha_inscripcion')

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ('id','clase','alumno','nota','ponderacion','observacion')

    def validate_nota(self, valor):
        if valor < 1 or valor > 7:
            raise serializers.ValidationError("La nota debe estar entre 1.0 y 7.0")
        return valor

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('id','clase','alumno','fecha','presente','justificado')

class RegistroAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAuditoria
        fields = ('id','usuario_responsable','entidad_afectada','id_registro','tipo_evento','descripcion','created_at')
