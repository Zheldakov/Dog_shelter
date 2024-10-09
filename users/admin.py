from django.contrib import admin
from users.models import User
# Регистрируем модель User в административной панели Django
admin.site.register(User)
