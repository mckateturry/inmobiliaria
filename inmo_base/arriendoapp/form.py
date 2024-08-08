from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class CrearUsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, help_text='Nombre de usuario')
    first_name = forms.CharField(max_length=30, required=True, help_text='Nombre')
    last_name = forms.CharField(max_length=30, required=True, help_text='Apellido')
    address = forms.CharField(max_length=255, required=True, help_text='Dirección')
    phone = forms.CharField(max_length=15, required=True, help_text='Teléfono')
    email = forms.EmailField(max_length=254, required=True, help_text='Correo electrónico')
    password = forms.CharField(widget=forms.PasswordInput(), required=True, help_text='Contraseña')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'address', 'phone', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user





class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['direccion', 'telefono', 'correo_electronico']



#CREAR IMAGEN
class ImageUploadForm(forms.Form):
    image_url = forms.URLField(
        label='URL de la Imagen',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://ejemplo.com/imagen.jpg'})
    )
    description = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe una descripción aquí...'})
    )
    style = forms.ChoiceField(
        label='Estilo',
        choices=[
            ('artistic', 'Artístico'),
            ('landscape', 'Paisaje'),
            ('portrait', 'Retrato'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )