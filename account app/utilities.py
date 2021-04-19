from django.template.loader import render_to_string
# импорт класса Signer для формирование электронной подписи(акстивации) пользователя
# import of the Signer class to generate an electronic signature (activation) of the user
from django.core.signing import Signer
# импорт списка ALLOWED_HOSTS для извлечение домена страници акстивации
# import the ALLOWED_HOSTS list to extract the domain of the activation page
from pipa.settings import ALLOWED_HOSTS


signer = Signer()


# определение метода для формирования и отправки письма для активации нового пользователя
# definition of a method for generating and sending a letter to activate a new user
def send_activation_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)
