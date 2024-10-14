from django import forms

from dogs.models import Dog

class DogForm(forms.ModelForm):
    # Создаем форму для добавления/редактирования питомца с указанными полями
    class Meta:
        model = Dog
        fields = '__all__'
