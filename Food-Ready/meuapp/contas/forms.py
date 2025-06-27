from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    """
    Formulário de autenticação customizado com placeholders em português.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Nome de usuário ou Email'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Senha'}
        )

class CustomUserCreationForm(UserCreationForm):
    """
    Formulário de criação de usuário customizado com placeholders em português.
    O formulário do Figma inclui um campo de Email, que não existe por padrão.
    Para simplificar, usaremos o 'username' como "Nome" e adicionaremos um campo de email.
    """
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Nome'}
        )
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email'}
        )
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Senha'}
        )
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirmar Senha'}
        )