from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('', views.user_login, name='login'),
  path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
  path('index/', views.index, name='index'),
  path('home', views.home, name='home'),
  path('crear_resultado', views.crear_resultado, name='crear_resultado'),
  path('modificar_resultado/<int:resultado_id>', views.modificar_resultado, name='modificar_resultado'),
  path('eliminar_resultado/<int:resultado_id>', views.eliminar_resultado, name='eliminar_resultado'),
  path('home/ver_actividad/<int:resultado_id>', views.ver_actividad, name='ver_actividad'),
  path('home/ver_actividad/crear_actividad', views.crear_actividad, name='crear_actividad'),
]
