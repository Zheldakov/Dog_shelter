from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from dogs.models import Category, Dog
from django.urls import reverse
from dogs.forms import DogForm


def index(request):
    """ Показывает главную страницу с информацией о категориях и питомниках."""
    context = {
        'object_list': Category.objects.all()[:3],
        'title': "Питомник - Главная"
    }
    return render(request, 'dogs\index.html', context)


def categories(request):
    """ Показывает страницу с информацией о всех категориях питомника."""
    context = {
        'object_list': Category.objects.all(),
        'title': "Питомник - Все наши породы"
    }
    return render(request, 'dogs\categories.html', context)


def category_dogs(request, pk):
    """ Показывает страницу с информацией о питомцах определенной категории."""
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Dog.objects.filter(category_id=pk),
        'title': f'Собаки породы {category_item.name}',
        'category_pk': category_item.pk,
    }
    return render(request, 'dogs\dogs.html', context)


def dogs_list_view(request):
    """ Показывает страницу со списком всех питомцев."""
    context = {
        'object_list': Dog.objects.all(),
        'title': "Питомник - Все наши собаки"
    }
    return render(request, 'dogs\dogs_list_view.html', context) # пока как я понимаю нет
    # return render(request, 'dogs\dogs.html', context) # тестовый вариант


def dog_create_view(request):
    """ Страница создания нового питомца."""
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)  # Валидация формы
        if form.is_valid():  # Если форма валидна, сохраняем данные
            dog = form.save()  # Сохраняем питомца в базе
            return HttpResponseRedirect(reverse('dogs:list_dogs'))  # Переходим на страницу детальной информации питомца
    return render(request, 'dogs\create.html', {'form': DogForm()})  # Отображаем форму создания питомца
