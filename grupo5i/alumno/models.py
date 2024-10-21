from django.db import models

# Create your models here.

class Alumno(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="apellido paterno jajajaja")
    amaterno=models.CharField(max_length=50,verbose_name="apellido materno")
    nombre=models.CharField(max_length=100,verbose_name="nombre (s)")
    fecha_nacimiento=models.DateField(verbose_name="fecha de nacimiento",null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name="fecha de ingreso",null=False,blank=False)

class Meta:
    db_table="Alumno"
    verbose_name="Alumno"
    verbose_name_plural="Alumnos"

    def __str__(self) -> str:
        return self.nombre

class Frase(models.Model):
    comentario=models.TextField(verbose_name="comentario",max_length=400)
    Alumno_fk=models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Frase"
        verbose_name_plural="Frases"