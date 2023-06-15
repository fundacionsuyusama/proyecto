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
  path('home/resultado/<int:resultado_id>', views.ver_actividad, name='ver_actividad'),
  path('home/resultado/<int:resultado_id>/crear_actividad', views.crear_actividad, name='crear_actividad'),
  path('home/resultado/<int:resultado_id>/editar/<int:actividad_id>', views.editar_actividad, name='editar_actividad'),
  path('home/resultado/<int:resultado_id>/eliminar/<int:actividad_id>', views.eliminra_actividad, name='eliminra_actividad'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion', views.ver_secciones, name='ver_secciones'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/guardar', views.guardar_seccion, name='guardar_seccion'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion/crear_secciones', views.crear_secciones, name='crear_secciones'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion/editar_seccion/<int:id>', views.editar_secciones, name='editar_secciones'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion/eliminar_seccion/<int:id>', views.eliminar_secciones, name='eliminar_secciones'),
]