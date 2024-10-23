from django import forms

from dogs.models import Dog
from users.forms import StyleFromMixin

class DogForm(StyleFromMixin,forms.ModelForm):
    # Создаем форму для добавления/редактирования питомца с указанными полями
    class Meta:
        model = Dog
        fields = '__all__'
