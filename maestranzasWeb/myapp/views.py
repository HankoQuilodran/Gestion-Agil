from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Categoria  # Asegúrate de importar ambos modelos
from django.contrib.auth.models import User
def index(request):
    return render(request, 'index.html')

def crear_productos_iniciales():
    productos_iniciales = [
        {'nombre': "Martillo de Acero", 'descripcion': "Martillo profesional con mango de fibra de vidrio",'precio': 12500,'imagen': "martillo.png", 'stock': 50},
        {'nombre': "Destornillador Phillips", 'descripcion': "Juego de destornilladores anti-deslizantes", 'precio': 8500,'imagen': "martillo.png", 'stock': 120},
        {'nombre': "Taladro Percutor 750W", 'descripcion': "Taladro con percusión y velocidad variable", 'precio': 45900,'imagen': "martillo.png", 'stock': 15},
        {'nombre': "Sierra Circular 1800W", 'descripcion': "Sierra circular profesional con láser guía", 'precio': 78900,'imagen': "martillo.png", 'stock': 8},
        {'nombre': "Llave Inglesa Ajustable", 'descripcion': "Llave de 8 a 32 mm con cabeza giratoria", 'precio': 15600,'imagen': "martillo.png", 'stock': 45},
        {'nombre': "Cemento Gris 25kg", 'descripcion': "Cemento de fraguado normal para construcción", 'precio': 8500,'imagen': "martillo.png", 'stock': 200},
        {'nombre': "Ladrillo Fiscal 6 huecos", 'descripcion': "Ladrillo cerámico estándar 6 huecos", 'precio': 350,'imagen': "martillo.png", 'stock': 1000},
        {'nombre': "Pintura Latex 4L", 'descripcion': "Pintura blanca lavable interior/exterior", 'precio': 22900,'imagen': "martillo.png", 'stock': 30},
        {'nombre': "Cerámica 45x45 cm", 'descripcion': "Piso cerámico antideslizante", 'precio': 8990,'imagen': "martillo.png", 'stock': 150},
        {'nombre': "Tubo PVC 1/2\" x 3m", 'descripcion': "Tubería para instalaciones sanitarias", 'precio': 3200,'imagen': "martillo.png", 'stock': 80},
        {'nombre': "Cable Eléctrico 2.5mm", 'descripcion': "Cobre flexible para instalaciones", 'precio': 4500,'imagen': "martillo.png", 'stock': 120},
        {'nombre': "Interruptor Simple", 'descripcion': "Interruptor de pared para 10A", 'precio': 2500,'imagen': "martillo.png", 'stock': 60},
        {'nombre': "Lijadora Orbital", 'descripcion': "Lijadora profesional 250W con bolsa colectora", 'precio': 38900,'imagen': "martillo.png", 'stock': 12},
        {'nombre': "Nivel Laser", 'descripcion': "Nivel láser autónivelante 360°", 'precio': 65900,'imagen': "NivelLaser360.jpg", 'stock': 5},
        {'nombre': "Andamio Modular", 'descripcion': "Estructura metálica para trabajo en altura", 'precio': 125000,'imagen': "andamio.jpg", 'stock': 3},
        {'nombre': "Carretilla de Obra", 'descripcion': "Carretilla metálica 6 pies cúbicos", 'precio': 45900,'imagen': "martillo.png", 'stock': 18},
        {'nombre': "Mezcladora de Pintura", 'descripcion': "Accesorio para taladro para mezclar pintura", 'precio': 8900,'imagen': "martillo.png", 'stock': 25},
        {'nombre': "Broca para Concreto 1/2\"", 'descripcion': "Juego de brocas widia para concreto", 'precio': 12900,'imagen': "martillo.png", 'stock': 40},
        {'nombre': "Guantes de Seguridad", 'descripcion': "Guantes anticorte nivel 5", 'precio': 9900,'imagen': "martillo.png", 'stock': 75},
        {'nombre': "Casco de Seguridad", 'descripcion': "Casco con ajuste ergonómico y visera", 'precio': 7500,'imagen': "martillo.png", 'stock': 50}
    ]
    
    for prod in productos_iniciales:
        if not Producto.objects.filter(nombre=prod['nombre']).exists():
            Producto.objects.create(**prod)

def catalogo(request):
    crear_productos_iniciales()  # Esta función asegura que los productos existan
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'catalogo.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})



def admin_panel(request):
    return render(request, 'admin-panel.html', {
        'productos': Producto.objects.all(),
        'usuarios': User.objects.all()  # Add this line
    })
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})