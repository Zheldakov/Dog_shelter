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
    # return render(request, 'dogs\dogs_list_view.html', context)  # пока как я понимаю нет
    return render(request, 'dogs\dogs.html', context) # тестовый вариант


def dog_create_view(request):
    """ Страница создания нового питомца."""
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)  # Валидация формы
        if form.is_valid():  # Если форма валидна, сохраняем данные
            dog = form.save()  # Сохраняем питомца в базе
            return HttpResponseRedirect(reverse('dogs:list_dogs'))  # Переходим на страницу детальной информации питомца
    return render(request, 'dogs\create.html', {'form': DogForm()}, )  # Отображаем форму создания питомца


def dog_detail_view(request, pk):
    """ Показывает страницу детальной информации о питомце."""
    dog_item = get_object_or_404(Dog, pk=pk)  # Получаем питомца из базы по pk /самодеятельность
    context = {
        'object': Dog.objects.get(pk=pk),  # Получаем питомца из базы по pk,
        'title': f'Детальная информация о собаке {dog_item.name}'
    }
    return render(request, 'dogs\detail.html', context)


def dog_update_view(request, pk):
    """ Страница редактирования питомца."""
    # dog_object = Dog.objects.get(pk=pk)  # Получаем питомца из базы по(тоже что и ниже)
    dog_object = get_object_or_404(Dog, pk=pk)  # Получаем питомца из базы по pk
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog_object)  # Валидация формы
        if form.is_valid():  # Если форма валидна, сохраняем данные
            dog_object = form.save()  # Сохраняем питомца в базе
            dog_object.save()  # Сохраняем питомца в базе
            return HttpResponseRedirect(reverse('dogs:detail_dog', args={pk: pk}))  #
    return render(request, 'dogs/update.html', {'object': dog_object, 'form': DogForm(instance=dog_object)}, )  # Отображаем форму создания питомца


def dog_delete_view(request, pk):
    dog_object = get_object_or_404(Dog, pk=pk)  # Получаем питомца из базы по pk
    if request.method == 'POST':  # Если запрос POST
        dog_object.delete()  # Удаляем питомца из базы
        return HttpResponseRedirect(reverse('dogs:list_dogs'))  # Переходим на страницу со списком питомцев
    return render(request, 'dogs/delete.html', {
        'object': dog_object}, )  # Отображаем страницу подтверждения удаления
