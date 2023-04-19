from django.urls import path
from login import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    path('login', views.login_request, name="Login"),
    path('', views.inicio, name='inicio'),
    path('register', views.register, name='register'),
    #path('logout', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    path('login', LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    
    ]