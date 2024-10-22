from django import forms

from users.models import User


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFromMixin, forms.ModelForm):
    """Форма редактирования профиля пользователя."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone',)


class UserRegisterForm(StyleFromMixin, forms.ModelForm):
    """ Форма для регистрации нового пользователя."""
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        # Поля модели User
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Проверка соответствия паролей
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserLoginForm(StyleFromMixin, forms.Form):
    """ Форма для авторизации пользователя."""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)