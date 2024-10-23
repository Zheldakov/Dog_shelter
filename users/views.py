from lib2to3.fixes.fix_input import context

from django.shortcuts import reverse, render, redirect

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm


def user_register_view(request):
    # Вывод формы регистрации
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():  # Если форма валидна, сохраняем данные
            new_user = form.save()  # Получаем нового пользователя
            new_user.set_password(form.cleaned_data['password'])  # Установка пароля
            new_user.save()  # Сохраняем нового пользователя
            return HttpResponseRedirect(reverse('users:login_user'))  # Переход на главную страницу питомника
    context = {'form': form}
    return render(request, 'user/register_user.html', context)


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

    form = UserLoginForm()
    context = {
        'form': form}
    return render(request, 'user/login_user.html', context)


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


def user_logout_view(request):
    # выход из системы
    logout(request)
    return redirect('dogs:index')


@login_required
def user_update_view(request):
    # изменение профиля пользователя
    user_object = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
        if form.is_valid():
            user_object = form.save()
            user_object.save()
            return HttpResponseRedirect(reverse('users:profile_user'))
    user_name = user_object.first_name
    context = {
        'user_object': user_object,
        'title': f'Изменение профиля {user_name}',
        'form': UserUpdateForm(instance=user_object),
    }
    return render(request, 'user/update_user.html', context)
