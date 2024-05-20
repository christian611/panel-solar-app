from django.shortcuts import render

from app.models import Producto

# Create your views here.

def mostrarIndex(request):
    return render(request, 'index.html')


def mostrarInfo(request):
    return render(request, 'info.html')


def mostrarListado(request): 
    pro = Producto.objects.all().values()
    datos = {'pro' : pro }
    return render(request, 'listado.html', datos)

    
def mostrarFormRegistrar(request):
    return render(request, 'form_registrar.html')


def mostrarFormActualizar(request, id):
    try:
        pro = Producto.objects.get(id = id)
        datos = { 'pro' : pro }
        return render(request, 'form_actualizar.html', datos)
    except:
        pro = Producto.objects.all().values()
        datos = { 
            'pro' : pro, 
            'r2' : 'El ID ('+str(id)+') No Existe. Imposible Actualizar!!' 
        }
        return render(request, 'listado.html', datos)



def insertarProducto(request):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        mar = request.POST['cbomar']
        tipo = request.POST['txttipo']
        pre = request.POST['txtpre']
        proy = request.POST['txtproy']
        eva = request.POST['txteva']
        pa = request.POST['txtpa'] 
        pro = Producto(nombre = nom, vivienda = mar, tipo = tipo, precio = pre, proyeccion = proy, consumo = eva, panel = pa )
        pro.save()
        datos = {'r' : 'Registro Realizado Correctamente'}
        return render(request, 'form_registrar.html', datos)
    else:
        datos = {'r2' : 'No se puede solicitar solicitud'}
        return render(request, 'form_registrar.html', datos)


def actualizarProducto(request, id):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        mar = request.POST['cbomar']
        tipo = request.POST['txttipo']
        pre = request.POST['txtpre']
        proy = request.POST['txtproy']
        eva = request.POST['txteva']
        pa = request.POST['txtpa'] 
        pro = Producto.objects.get(id = id)
        pro.nombre = nom
        pro.vivienda = mar
        pro.tipo = tipo
        pro.precio = pre
        pro.proyeccion = proy
        pro.consumo = eva 
        pro.panel = pa 
        pro.save()
        pro = Producto.objects.all().values()
        datos = { 
            'pro' : pro,
            'r' : 'Datos Modificados Correctamente!!' 
            }
        return render(request, 'listado.html', datos)
    else:
        datos = { 'r2' : 'No Se Puede Procesar Solicitud!!' }
        return render(request, 'listado.html', datos)


def eliminarProducto(request, id):
    try:
        pro = Producto.objects.get(id = id)
        pro.delete()
        pro = Producto.objects.all().values()
        datos = {
            'pro' : pro,
            'r' : 'Registro Eliminado Correctamente'
        }
        return render(request, 'listado.html', datos)
    except:
        pro = Producto.objects.all().values()
        datos = {
            'pro' : pro,
            'r2' : 'El ID ('+str(id)+') No Existe. Imposible Eliminar!!'
        }
        return render(request, 'listado.html', datos)


