from django.shortcuts import reverse

from django.shortcuts import render
from django.http import HttpResponseRedirect

from users.models import User
from users.forms import UserRegisterForm


def user_register_view(request):
    # Проверка на POST-запросы
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # Если форма валидна, сохраняем данные
            new_user = form.save()  # Получаем нового пользователя
            new_user.set_password(form.cleaned_data['password'])  # Установка пароля
            new_user.save()  # Сохраняем нового пользователя
            return HttpResponseRedirect(reverse('dogs:index'))  # Переход на главную страницу питомника
    return render(request, 'user/register_user.html', {'form': UserRegisterForm}, )
