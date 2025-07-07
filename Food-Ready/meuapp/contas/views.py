from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# --- Autenticação ---
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')
    else:
        form = CustomAuthenticationForm()
    
    register_form = CustomUserCreationForm()
    return render(request, 'contas/login.html', {'login_form': form, 'register_form': register_form})

def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu')
    else:
        form = CustomUserCreationForm()
    
    login_form = CustomAuthenticationForm()
    return render(request, 'contas/login.html', {'login_form': login_form, 'register_form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# --- Navegação Principal ---
@login_required
def menu_view(request):
    return render(request, 'contas/menu.html')

@login_required
def restaurantes_view(request):
    return render(request, 'contas/restaurantes.html')

@login_required
def quiosques_view(request):
    return render(request, 'contas/quiosques.html')

@login_required
def promocoes_view(request):
    return render(request, 'contas/promocoes.html')

@login_required
def configuracoes_view(request):
    return render(request, 'contas/configuracoes.html')

# --- Detalhes dos Restaurantes e Quiosques ---
@login_required
def lemax_detail_view(request):
    return render(request, 'contas/lemax_detail.html')

@login_required
def rei_do_mate_detail_view(request):
    return render(request, 'contas/rei_do_mate_detail.html')

@login_required
def porto_do_sabor_detail_view(request):
    return render(request, 'contas/porto_do_sabor_detail.html')

@login_required
def megamatte_detail_view(request):
    return render(request, 'contas/megamatte_detail.html')

@login_required
def na_medida_detail_view(request):
    return render(request, 'contas/na_medida_detail.html')

@login_required
def strogonoff_detail_view(request):
    return render(request, 'contas/strogonoff_detail.html')

@login_required
def acai_do_jhonny_detail_view(request):
    return render(request, 'contas/acai_do_jhonny_detail.html')

@login_required
def kakumi_cozinha_detail_view(request):
    return render(request, 'contas/kakumi_cozinha_detail.html')

# CORRIGIDO: A nova view está aqui, com a indentação correta.
@login_required
def tia_zeze_detail_view(request):
    return render(request, 'contas/tia_zeze_detail.html')

# --- Lógica do Carrinho ---
@login_required
def add_carrinho_view(request, produto_nome, produto_preco):
    carrinho = request.session.get('carrinho', {})
    produto_preco = float(produto_preco.replace(',', '.'))

    if produto_nome in carrinho:
        carrinho[produto_nome]['quantidade'] += 1
    else:
        carrinho[produto_nome] = {'preco': produto_preco, 'quantidade': 1}
    
    request.session['last_restaurant_url'] = request.META.get('HTTP_REFERER', reverse('restaurantes'))
    
    request.session['carrinho'] = carrinho
    return redirect('carrinho')

@login_required
def atualizar_carrinho_view(request, produto_nome, action):
    carrinho = request.session.get('carrinho', {})

    if produto_nome in carrinho:
        if action == 'adicionar':
            carrinho[produto_nome]['quantidade'] += 1
        elif action == 'remover':
            carrinho[produto_nome]['quantidade'] -= 1
            if carrinho[produto_nome]['quantidade'] <= 0:
                del carrinho[produto_nome]
    
    request.session['carrinho'] = carrinho
    return redirect('carrinho')

@login_required
def carrinho_view(request):
    carrinho = request.session.get('carrinho', {})
    total_carrinho = 0
    for item in carrinho.values():
        total_carrinho += item.get('preco', 0) * item.get('quantidade', 0)

    last_restaurant_url = request.session.get('last_restaurant_url', reverse('restaurantes'))

    context = {
        'carrinho': carrinho,
        'total_carrinho': total_carrinho,
        'last_restaurant_url': last_restaurant_url,
    }
    return render(request, 'contas/carrinho.html', context)

@login_required
def finalizar_compra_view(request):
    carrinho = request.session.get('carrinho', {})
    if not carrinho:
        return redirect('carrinho')
        
    total_carrinho = 0
    for item in carrinho.values():
        total_carrinho += item.get('preco', 0) * item.get('quantidade', 0)

    context = {
        'total_carrinho': total_carrinho,
    }
    return render(request, 'contas/finalizar_compra.html', context)

@login_required
def good_burger_detail_view(request):
    return render(request, 'contas/good_burger_detail.html')

