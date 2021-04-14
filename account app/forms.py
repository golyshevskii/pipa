# импорт объекта forms
# import object forms
from django import forms
# импорт объектов User, UserCreationForm, Profile для создания формы регистрации и настроек пользователя
# import objects User, UserCreationForm, Profile to create registration form and user settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# класс LoginForm для создания формы входа на веб-сайт + наследование объектов класса Form
# class LoginForm to create a login form for the website + inheritance of objects of the Form class
class LoginForm(forms.Form):        
    # определение полей для логина и пароля
    # defining fields for login and password
    username = forms.CharField()             
    password = forms.CharField(widget=forms.PasswordInput)  # ключ widget для скрытия ввода пароля пользователем; widget key to hide user password input

# форма для регистрации пользователя
# user registration form
class UserRegistrationForm(UserCreationForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)  # поле для ввода пароля; field for entering password
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput)  # повторное поле для пароля; repeated password entry field

    # опции класса UserRegistrationForm
    # class options UserRegistrationForm
    class Meta:
        # объявление модели User, которая содержит в себе необходимые поля для заполнения формы
        # declaration of the User model, which contains the necessary fields to fill out the form
        model = User
        # выбор полей из модели User, которые будут включены в форму
        # selection of fields from the User model that will be included in the form
        fields = ('username', 'email')

    # определение метода для проверки на равенство паролей в поле password и password2
    # definition of a method for checking for equality of passwords in the password and password2 fields
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("ops! passwords don't match")
        return cd['password2']

    
# класс для создания формы настроек пользователя
# class for creating user settings form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# класс для создания формы настроек пользователя
# class for creating user settings form
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
