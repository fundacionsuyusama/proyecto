from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('', views.user_login, name='user_login'),
  path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
  path('index/', views.index, name='index'),
  path('home', views.home, name='home'),
  path('exportar_datos', views.exportar_datos, name='exportar_datos'),
  path('exportar_datos/export', views.exportar, name='exportar'),
  path('progreso', views.progreso, name='progreso'),
  path('crear_resultado', views.crear_resultado, name='crear_resultado'),
  path('modificar_resultado/<int:resultado_id>', views.modificar_resultado, name='modificar_resultado'),
  path('eliminar_resultado/<int:resultado_id>', views.eliminar_resultado, name='eliminar_resultado'),
  path('home/resultado/<int:resultado_id>', views.ver_actividad, name='ver_actividad'),
  path('home/resultado/<int:resultado_id>/crear_actividad', views.crear_actividad, name='crear_actividad'),
  path('home/resultado/<int:resultado_id>/editar/<int:actividad_id>', views.editar_actividad, name='editar_actividad'),
  path('home/resultado/<int:resultado_id>/eliminar/<int:actividad_id>', views.eliminra_actividad, name='eliminra_actividad'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/crear_avance', views.crear_avance, name='crear_avance'),
  # Estoy aquí
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/crear_fecha', views.crear_cumplida, name='crear_cumplida'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/crear_proceso', views.crear_proceso, name='crear_proceso'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/crear_urgente', views.crear_urgente, name='crear_urgente'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/editar_avance/<int:id>', views.editar_avance, name='editar_avance'),
  # Ahora aqui
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/editar_fecha/<int:id>', views.editar_cumplida, name='editar_cumplida'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/editar_proceso/<int:id>', views.editar_proceso, name='editar_proceso'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/editar_urgente/<int:id>', views.editar_urgente, name='editar_urgente'),

  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/eliminar_avance/<int:id>', views.eliminar_avance, name='eliminar_avance'),
  # Esto aqui
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/eliminar_fecha/<int:id>', views.eliminar_cumplida, name='eliminar_cumplida'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/eliminar_proceso/<int:id>', views.eliminar_proceso, name='eliminar_proceso'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/eliminar_urgente/<int:id>', views.eliminar_urgente, name='eliminar_urgente'),

  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/eliminar_dificultad/<int:id>', views.eliminar_dificultad, name='eliminar_dificultad'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/crear_dificultad', views.crear_dificultad, name='crear_dificultad'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/editar_dificultad/<int:id>', views.editar_dificultad, name='editar_dificultad'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/dificultad/<int:dificultad_id>/crear_alternativa', views.crear_alternativa, name='crear_alternativa'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/dificultad/<int:dificultad_id>/editar_alternativa/<int:id>', views.editar_alternativa, name='editar_alternativa'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/dificultad/<int:dificultad_id>/eliminar_alternativa/<int:id>', views.eliminar_alternativa, name='eliminar_alternativa'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion', views.ver_secciones, name='ver_secciones'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/guardar', views.guardar_seccion, name='guardar_seccion'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion/crear_secciones', views.crear_secciones, name='crear_secciones'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion/editar_seccion/<int:id>', views.editar_secciones, name='editar_secciones'),
  path('home/resultado/<int:resultado_id>/actividad/<int:actividad_id>/seccion/eliminar_seccion/<int:id>', views.eliminar_secciones, name='eliminar_secciones'),
]