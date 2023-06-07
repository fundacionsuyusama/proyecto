from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('', views.user_login, name='login'),
  path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
  path('index/', views.index, name='index'),
  path('home/', views.home, name='home'),
  path('crear_resultado/', views.crear_resultado, name='crear_resultado'),
]
