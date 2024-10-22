from django.shortcuts import reverse, render

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserForm


def user_register_view(request):
    # Вывод формы регестрации
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # Если форма валидна, сохраняем данные
            new_user = form.save()  # Получаем нового пользователя
            new_user.set_password(form.cleaned_data['password'])  # Установка пароля
            new_user.save()  # Сохраняем нового пользователя
            return HttpResponseRedirect(reverse('users:login_user'))  # Переход на главную страницу питомника
    return render(request, 'user/register_user.html', {'form': UserRegisterForm}, )


def user_login_view(request):
    # Выводим форму логина
    if request.method == 'POST':
        form = UserLoginForm(request.POST)  # Создаем экземпляр формы
        if form.is_valid():  # Если форма валидна
            cd = form.cleaned_data  # Очищаем данные
            user = authenticate(email=cd['email'], password=cd['password'])  # Аутентифицируем пользователя
            if user is not None:  # Если пользователь существует
                if user.is_active:  # Если пользователь активен
                    login(request, user)  # Авторизуем пользователя
                    return HttpResponseRedirect(reverse('dogs:index'))  # Переход на главную страницу питомника
                else:
                    return HttpResponse('Аккаунт не активен')


    else:
        # если запрос GET, то рендерим форму входа
        form = UserLoginForm()
    return render(request, 'user/login_user.html', {'form': form})


@login_required
def user_profile_view(request):
    # отображение профиля пользователя
    user_object = request.user
    context = {
        # 'user_object': user_object,
        'title': f'Ваш профиль {user_object.first_name}',
        # 'form': UserForm(instance=user_object),
    }
    return render(request, 'user/user_profile_read_only.html', context)
