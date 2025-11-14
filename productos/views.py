from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria

def inicio(request):
    return render(request, 'inicio.html')

def creditos(request):
    return render(request, 'creditos.html')

# Vistas de Categorías
def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('-fecha_creacion')
    return render(request, 'categorias/lista.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        Categoria.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('lista_categorias')
    return render(request, 'categorias/agregar.html')

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.save()
        return redirect('lista_categorias')
    return render(request, 'categorias/editar.html', {'categoria': categoria})

# Vistas de Productos
def lista_productos(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'productos/lista.html', {'productos': productos})

def agregar_producto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')
        
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria_id=categoria_id
        )
        return redirect('lista_productos')
    return render(request, 'productos/agregar.html', {'categorias': categorias})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.categoria_id = request.POST.get('categoria')
        producto.save()
        return redirect('lista_productos')
    return render(request, 'productos/editar.html', {'producto': producto, 'categorias': categorias})