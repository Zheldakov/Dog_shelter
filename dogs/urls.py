from django.urls import path
from dogs.views import index, categories, category_dogs, dogs_list_view, dog_create_view
from dogs.apps import DogsConfig

app_name = DogsConfig.name  # DogsConfig имя приложения

urlpatterns = [
    path('', index, name='index'),  # url на главную страницу
    path('categories/', categories, name='categories'),  # url на страницу с информацией о всех категориях
    path('categories/<int:pk>/dogs/', category_dogs, name='category_dogs'), # url на страницу с информацией о питомцах определенной кат
    path('dogs/', dogs_list_view, name='list_dogs'),  # url на страницу с информацией о всех питомцах (вместо pk)
    path('dogs/create',dog_create_view, name='create_dog'), # url на страницу создания нового питомца
]
