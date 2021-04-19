from django import forms
# импорт метода password_validation для проверки валидности пароля
# import password_validation method to check password validity
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import Profile
# импорт экземпляра user_registered для отправки сообщения пользователю с ссылкой активации аккаунта
# import of user_registered instance to send a message to the user with an account activation link
from .apps import user_registered


# форма для регистрации пользователя
# user registration form
class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput)

    # метод clean_password1 для проверки валидности пароля1
    # method clean_password1 to check if password1 is valid
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    # метод clean для проверки равенства двух паролей
    # clean method to check if two passwords are equal
    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError("ops! passwords didn't match", code='password_mismatch')}
            raise ValidationError(errors)

    # медот для предварительного сохранения данных о новом пользователе
    # method for pre-saving data about a new user
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False     # определение ключей активности и активации пользователя
        user.is_activated = False  # defining the keys of activity and activation of the user
        if commit:
            user.save()
        # сигнал для отправки сообщения пользователю с ссылкой активации аккаунта
        # signal to send a message to the user with an account activation link
        user_registered.send(UserRegistrationForm, instance=user)
        return user
    
    # нстройки класса; class settings
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2')

    
# класс для создания формы настроек пользователя
# class for creating user settings form
class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email',
                  'date_of_birth', 'photo')
