# Generated by Django 5.0.7 on 2024-08-02 18:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.FloatField()),
                ('m2_totales', models.FloatField()),
                ('cantidad_estacionamientos', models.IntegerField()),
                ('cantidad_habitaciones', models.IntegerField()),
                ('cantidad_banos', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('precio_mensual', models.IntegerField()),
                ('imagen_url', models.URLField(blank=True, default='https://guttche.cl/wp-content/uploads/2024/01/sinfoto.png', null=True)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.comuna')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.region')),
                ('tipo_inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.tipoinmueble')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.region'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(default='default@example.com', max_length=255)),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.tipousuario')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudArriendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.TextField()),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.inmueble')),
                ('arrendatario', models.ForeignKey(limit_choices_to={'tipo_usuario__name': 'arrendatario'}, on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='inmueble',
            name='arrendador',
            field=models.ForeignKey(limit_choices_to={'tipo_usuario__name': 'anfitrion'}, on_delete=django.db.models.deletion.CASCADE, to='arriendoapp.usuario'),
        ),
    ]
