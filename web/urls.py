from django.urls import path
from web import views
from django.contrib.auth.views import LogoutView,LoginView




urlpatterns = [
    path('',views.inicio, name="Inicio"), #este era nuestro primer view
    path('pistolas',views.Pistolas,name="pistolas"),
    path('asalto',views.asalto,name="asalto"),
    path('dmr',views.dmr,name="dmr"),
    #path('pistolaformulario/', views.PistolaFormulario,name="pistolaformulario"),
   # path('asaltoformulario/', views.AsaltoFormulario,name="asaltoformulario"),
   # path('dmrformulario/', views.DmrFormulario,name="dmrformulario"),
    path('busquedapistola', views.busquedapistola,name="busquedapistola"),
    path('busca/',views.buscar),
    path('leerpistola/', views.leerpistola,name = "leerpistola"),
    path('editarpistola/<pistola_nombre>/', views.editarpistola, name="editarpistola"),
    path('leerasalto/', views.leerasalto,name = "leerasalto"),
    path('eliminarasalto/<aSalto_nombre>/', views.eliminarasalto, name="Eliminarasalto"),
    path('editarasalto/<aSalto_nombre>/', views.editarasalto, name="editarasalto"),
    #login de sistema
    #path('login', views.login_request, name="Login"),
    #path('', views.inicio, name='inicio'),
    #path('register', views.register, name='register'),
    #path('logout', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    #path('login', LoginView.as_view(), name='login'),
    #path('logout/', views.logout_view, name='logout'),
]
