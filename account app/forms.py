# импорт объекта forms
# import object forms
from django import forms


# класс LoginForm для создания формы входа на веб-сайт + наследование объектов класса Form
# class LoginForm to create a login form for the website + inheritance of objects of the Form class
class LoginForm(forms.Form):        
    # определение полей для логина и пароля
    # defining fields for login and password
    username = forms.CharField()             
    password = forms.CharField(widget=forms.PasswordInput)  # ключ widget для скрытия ввода пароля пользователем; widget key to hide user password input
