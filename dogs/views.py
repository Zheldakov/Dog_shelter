from django.shortcuts import render

from dogs.models import Category, Dog


def index(request):
    """ Показывает главную страницу с информацией о категориях и питомниках."""
    context = {
        'objects_list': Category.objects.all()[:3],
        'title': "Питомник - Главная"
    }
    return render(request, 'dogs\index.html', context)

def categories(request):
    """ Показывает страницу с информацией о всех категориях питомника."""
    context = {
        'objects_list': Category.objects.all(),
        'title': "Питомник - Все наши породы"
    }
    return render(request, 'dogs\categories.html', context)

def category_dogs(request, pk):
    """ Показывает страницу с информацией о питомцах определенной категории."""
    category_item = Category.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(category_id=pk),
        'title': f'Собаки породы {category_item.name}',
        'category_pk': category_item.pk,
    }
    return render(request, 'dogs\dogs.html', context)