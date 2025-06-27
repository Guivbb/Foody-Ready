# Arquivo: contas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('menu/', views.menu_view, name='menu'),
    path('restaurantes/', views.restaurantes_view, name='restaurantes'),
    path('quiosques/', views.quiosques_view, name='quiosques'),
    path('restaurantes/lemax/', views.lemax_view, name='lemax_detail'),
    path('rei-do-mate/', views.rei_do_mate_detail_view, name='rei_do_mate_detail'),
    path('porto-do-sabor/', views.porto_do_sabor_detail_view, name='porto_do_sabor_detail'),
    path('megamatte/', views.megamatte_detail_view, name='megamatte_detail'),
]