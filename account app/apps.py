# импорт класса AppConfig для приложения account
# importing the AppConfig class for the account application
from django.apps import AppConfig
# импорт класса Signal и метода send_activation_notification для отправки сообщения об активации пользователю
# import of the Signal class and the send_activation_notification method to send an activation message to the user
from django.dispatch import Signal
from .utilities import send_activation_notification


# экземпляр класса Signal для отправки сообщений об активации
# an instance of the Signal class to send activation messages
user_registered = Signal(providing_args=['instance'])


# диспетчер отправки сообщений
# dispatcher for sending messages
def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatcher)


class AccountConfig(AppConfig):
    name = 'account'
