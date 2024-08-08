from django.db import models
from django.contrib.auth.models import User

class Region(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return f"({self.id}) - {self.name}"

class Comuna(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"({self.id}) - {self.name} - region: {self.region.name}"

class TipoUsuario(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    descripcion = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self) -> str:
        return f"({self.id}) - {self.name}"

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=20, null=False, blank=False)  # Added max_length
    direccion = models.CharField(max_length=255, null=False, blank=False)  # Added max_length
    telefono = models.CharField(max_length=20, null=False, blank=False)  # Added max_length
    correo_electronico = models.EmailField(max_length=255, default='default@example.com')
    tipo_usuario = models.ForeignKey(TipoUsuario, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"({self.user}) {self.user.first_name}"

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self) -> str:
        return f"({self.id}) - {self.nombre}"

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=255)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)
    precio_mensual = models.IntegerField(null=False, blank=False)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario__name': 'anfitrion'})  # Corrected filter
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    imagen_url = models.URLField(max_length=200, null=True, blank=True, default='https://guttche.cl/wp-content/uploads/2024/01/sinfoto.png')

    def __str__(self):
        return f"{self.nombre} en {self.comuna.name}, {self.region.name}. Publicado por {self.arrendador.user.first_name}"

class SolicitudArriendo(models.Model):
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario__name': 'arrendatario'})  # Corrected filter
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"A {self.arrendatario.user.first_name} le interesa {self.inmueble.nombre}"
    
    
class Image(models.Model):
    image_url = models.URLField()
    description = models.TextField()
    style = models.CharField(max_length=20, choices=[('artistic', 'Artístico'), ('landscape', 'Paisaje'), ('portrait', 'Retrato')])
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Cambia 1 al ID del usuario predeterminado

    def __str__(self):
        return self.description
