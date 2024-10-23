from django.conf import settings
from django.core.mail import send_mail

def send_register_email(email):
    # Отправка письма при регистрации
    send_mail(
    subject="Поздравляем с регистрацией",#
        message=f"Вы зарегистрированы на сайте Dog Shelter",
        from_email=settings.EMAIL_HOST_USER, # Email address
        recipient_list=[email],  # Список получателей
    )