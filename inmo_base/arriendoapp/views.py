from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .form import CrearUsuarioForm, ImageUploadForm
from .models import Usuario, Image

# Create your views here.

def index(request):
    return render(request, 'index.html')

def lovit(request):
    return render(request, 'lovit.html')

def modoanfitrion(request):
    return render(request, 'modoanfitrion.html')

def modoviajero(request):
    return render(request, 'modoviajero.html')

def register(request): #def registrar_usuario(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de login después de crear el usuario
    else:
        form = CrearUsuarioForm()
    return render(request, 'register.html', {'form': form})


@login_required
def signout(request):
    logout(request)
    return redirect('index')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', 
                          {"form": AuthenticationForm, "error": "Usuario o contraseña incorrectos."})

        login(request, user)
        return redirect('lovit')
    
def register_img(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST)
        if form.is_valid():
            image_url = form.cleaned_data['image_url']
            description = form.cleaned_data['description']
            style = form.cleaned_data['style']
            
            # Guardar la imagen en la base de datos
            Image.objects.create(image_url=image_url, description=description, style=style)
            
            # Redirigir a la página de imágenes
            return redirect('imagenes')
    else:
        form = ImageUploadForm()

    return render(request, 'register_img.html', {'form': form})