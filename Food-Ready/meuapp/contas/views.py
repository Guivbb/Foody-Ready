from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Importando os formulários customizados do arquivo forms.py
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# View para a página de Login e Cadastro combinada
def login_view(request):
    # Usando os formulários customizados
    login_form = CustomAuthenticationForm(request)
    register_form = CustomUserCreationForm()

    if request.method == 'POST':
        # Verifica qual formulário foi enviado
        if 'login' in request.POST:
            login_form = CustomAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('menu')
        elif 'register' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('menu')

    context = {
        'login_form': login_form,
        'register_form': register_form,
    }
    return render(request, 'contas/login.html', context)

# Outras views (logout, menu, etc.) continuam aqui...
def logout_view(request):
    logout(request)
    return redirect('login')

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
def lemax_view(request):
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
def carrinho_view(request):
    return render(request, 'contas/carrinho.html')
