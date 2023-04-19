from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from web.forms import UserRegisterForm

# Create your views here.
def login_request(request):
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

def inicio(request):
    if request.user.is_authenticated:
        usuario = request.user.username
        return render(request, 'inicio.html', {'usuario': usuario})
    else:
        return redirect('login')
    # Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"register.html" ,  {"form":form})

def LogoutView(request):
    logout(request)
    return redirect('login')