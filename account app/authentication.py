from .models import Profile
from django.contrib.auth.backends import BaseBackend


# авторизация пользователя с помощью email
# user authorization using email
class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            # получение пользователя относительно введенного email
            # getting the user relative to the entered email
            user = Profile.objects.get(**kwargs)
            # если пароль в форме совпадает с паролем пользователя, то возвращаем пользователя
            # if the password in the form matches the user's password, then return the user
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    # получения пользователя относительно id
    # get user relative id
    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None
