from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend


# авторизация пользователя с помощью email
class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            # получение пользователя относительно введенного email
            user = User.objects.get(**kwargs)
            # если пароль в форме совпадает с паролем пользователя, то возвращаем пользователя
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    # получения пользователя относительно id
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
