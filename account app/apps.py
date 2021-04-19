# импорт класса AppConfig для приложения account
from django.apps import AppConfig
# импорт класса Signal и метода send_activation_notification для отправки сообщения об активации пользователю
from django.dispatch import Signal
from .utilities import send_activation_notification


user_registered = Signal(providing_args=['instance'])


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatcher)


class AccountConfig(AppConfig):
    name = 'account'
