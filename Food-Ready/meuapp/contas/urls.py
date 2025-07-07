from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('menu/', views.menu_view, name='menu'),
    path('restaurantes/', views.restaurantes_view, name='restaurantes'),
    path('quiosques/', views.quiosques_view, name='quiosques'),
    path('lemax/', views.lemax_detail_view, name='lemax_detail'),
    path('rei-do-mate/', views.rei_do_mate_detail_view, name='rei_do_mate_detail'),
    path('porto-do-sabor/', views.porto_do_sabor_detail_view, name='porto_do_sabor_detail'),
    path('megamatte/', views.megamatte_detail_view, name='megamatte_detail'),
    path('na-medida/', views.na_medida_detail_view, name='na_medida_detail'),
    path('strogonoff/', views.strogonoff_detail_view, name='strogonoff_detail'),
    path('acai-do-jhonny/', views.acai_do_jhonny_detail_view, name='acai_do_jhonny_detail'),
    path('kakumi-cozinha/', views.kakumi_cozinha_detail_view, name='kakumi_cozinha_detail'),
    path('tia-zeze/', views.tia_zeze_detail_view, name='tia_zeze_detail'),
    path('good-burger/', views.good_burger_detail_view, name='good_burger_detail'),
    path('promocoes/', views.promocoes_view, name='promocoes'),
    path('configuracoes/', views.configuracoes_view, name='configuracoes'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('finalizar-compra/', views.finalizar_compra_view, name='finalizar_compra'),
    path('add_carrinho/<path:produto_nome>/<str:produto_preco>/', views.add_carrinho_view, name='add_carrinho'),
    path('atualizar_carrinho/<path:produto_nome>/<str:action>/', views.atualizar_carrinho_view, name='atualizar_carrinho'),
]
