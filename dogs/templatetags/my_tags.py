"""
{% loads %}

"""

from  django import template

register = template.Library() # register

@register.filter()
def mymedia(val):
    """Фильтр для замены пути к медиафайлам на URL адрес из настроек MEDIA_URL."""
    if val:
        return fr"/media/{val}" # Если путь к медиафайлу не пустой, возвращаем его URL адрес
    return '/static/dummydog.jpg' # Если путь к медиафайлу пустой, возвращаем статический дефолтный изображение