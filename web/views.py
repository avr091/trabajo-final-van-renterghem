from django.shortcuts import render
from django.http import HttpResponse
from web.forms import PistolaFormulario ,AsaltoFormulario,DmrFormulario,UserRegisterForm
from web.models import pistolas,aSalto,dMr
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def inicio(request):
    
    return render(request,'inicio.html')

def Pistolas(request):
    if request.method == 'POST':
        miformulario= PistolaFormulario(request.POST)
       
        print(miformulario)

        if miformulario.is_valid():
                
                informacion=miformulario.cleaned_data
                
                Pistola=pistolas(nombre=informacion['nombre'],fps=informacion['fps'])
                
                Pistola.save()
                
                return render(request,"inicio.html")
    else:
         miformulario= PistolaFormulario()
    return render(request, 'pistolas.html', {'miformulario': miformulario})

#def asalto(request):
#    if request.method == 'POST':
#        miformulario=AsaltoFormulario(request.POST)
       
 #       print(miformulario)

  #      if miformulario.is_valid():
                
   #             informacion=miformulario.cleaned_data
                
    #            asalto=aSalto(nombre=informacion['nombre'],
     #           tipo=informacion['tipo'],
      #          fps=informacion['fps'])
                
       #         asalto.save()
                
        #        return render(request,"inicio.html")
   # else:
    #     miformulario= AsaltoFormulario()
    #return render(request, 'asalto.html', {'miformulario': miformulario})

from django.shortcuts import render, redirect


def asalto(request):
    if request.method == 'POST':
        miformulario = AsaltoFormulario(request.POST, request.FILES)

        if miformulario.is_valid():
            informacion = miformulario.cleaned_data

            # Obtener la imagen del formulario, si no se seleccionó imagen, asignar None
            imagen = request.FILES.get('imagen', None)

            # Si se cargó una imagen, crear una instancia de aSalto con la información del formulario y la imagen
            if imagen:
                asalto = aSalto(nombre=informacion['nombre'],
                                tipo=informacion['tipo'],
                                fps=informacion['fps'],
                                imagen=imagen)
            else:
                # Si no se cargó imagen, crear una instancia de aSalto con la información del formulario, sin imagen
                asalto = aSalto(nombre=informacion['nombre'],
                                tipo=informacion['tipo'],
                                fps=informacion['fps'])

            # Guardar la instancia en la base de datos
            asalto.save()

            # Redirigir a la página de inicio
            return redirect('inicio')

    else:
        miformulario = AsaltoFormulario()

    return render(request, 'asalto.html', {'miformulario': miformulario})




def dmr(request):
    if request.method == 'POST':
        miformulario=DmrFormulario(request.POST)
       
        print(miformulario)

        if miformulario.is_valid():
                
                informacion=miformulario.cleaned_data
                
                dmr=dMr(nombre=informacion['nombre'],
                tipo=informacion['tipo'],
                fps=informacion['fps'])
                
                dmr.save()
                
                return render(request,"inicio.html")
    else:
         miformulario= DmrFormulario()
    return render(request, 'dmr.html', {'miformulario': miformulario})

def busquedapistola(request):
     
     return render(request,"busquedapistola.html")
def buscar(request):
    if 'fps' in request.GET:
        fPs = request.GET['fps']
        PIstolas = pistolas.objects.filter(fps__icontains=fPs)
        return render(request, "resultadosporbusqueda.html", {"pistolas": PIstolas, "fps": fPs})
    else:
        respuesta = "no enviaste datos"
        return render(request, "inicio.html", {"respuesta": respuesta})
    
def leerpistola(request):
     
    lpistola = pistolas.objects.all() #trae todas las pistolas
    
    contexto= {"lpistola":lpistola}
    
    return render(request, "leerpistola.html",contexto)

def editarpistola(request, pistola_nombre):
    # Obtener la marcadora de pistola correspondiente
    marcadora = pistolas.objects.get(nombre=pistola_nombre)

    # Si se envió el formulario para guardar los cambios
    if request.method == "POST":
        # Obtener los datos enviados en el formulario
        nombre = request.POST.get("nombre")
        fps = request.POST.get("fps")
        
        # Actualizar los datos de la marcadora de asalto
        marcadora.nombre = nombre
        marcadora.fps = fps
        marcadora.save()

        # Redirigir al usuario a la página de detalles de la marcadora de asalto
        return redirect("leerpistola")

    # Si no se envió el formulario para guardar los cambios, mostrar el formulario de edición
    contexto = {"marcadora": marcadora}
    return render(request, "editarpistola.html", contexto)


def leerasalto(request):
     
    lasalto = aSalto.objects.all() #trae todos los asaltos
    
    contexto= {"lasalto":lasalto}
    
    return render(request, "leerasalto.html",contexto)


def eliminarasalto(request, aSalto_nombre):
    dasalto = aSalto.objects.get(nombre=aSalto_nombre)
    dasalto.delete()
    return redirect('leerasalto')

def editarasalto(request, aSalto_nombre):
    # Obtener la marcadora de asalto correspondiente
    marcadora = aSalto.objects.get(nombre=aSalto_nombre)

    # Si se envió el formulario para guardar los cambios
    if request.method == "POST":
        # Obtener los datos enviados en el formulario
        nombre = request.POST.get("nombre")
        fps = request.POST.get("fps")
        tipo = request.POST.get("tipo")

        # Actualizar los datos de la marcadora de asalto
        marcadora.nombre = nombre
        marcadora.fps = fps
        marcadora.tipo = tipo
        marcadora.save()

        # Redirigir al usuario a la página de detalles de la marcadora de asalto
        return redirect("leerasalto")

    # Si no se envió el formulario para guardar los cambios, mostrar el formulario de edición
    contexto = {"marcadora": marcadora}
    return render(request, "editarasalto.html", contexto)

#def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#def inicio(request):
    if request.user.is_authenticated:
        usuario = request.user.username
        return render(request, 'inicio.html', {'usuario': usuario})
    else:
        return redirect('login')
    # Vista de registro
#def register(request):

      #if request.method == 'POST':

            #form = UserCreationForm(request.POST)
          #  form = UserRegisterForm(request.POST)
          #  if form.is_valid():

           #       username = form.cleaned_data['username']
           #       form.save()
           ####return render(request,"register.html" ,  {"form":form})

#def logout_view(request):
    #logout(request)
    #return redirect('login')