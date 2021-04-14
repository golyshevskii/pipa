# импорт метода render для формирования представления на запрос пользователя
# import of the render method to generate a view for a user request
from django.shortcuts import render
# импорт метода authenticate для проверки валидности пользователя и метода login для авторизации пользователя в текущей сессии
# import of the authenticate method to check the validity of the user and the login method to authorize the user in the current session
from django.contrib.auth import authenticate, login
# импорт метода HttpResponse для отправки ответа об успешной авторизации пользователя или наоборот
# import of the HttpResponse method to send a response about successful user authorization or vice versa
from django.http import HttpResponse
# импорт класса LoginForm для предоставления формы пользователю
# import the LoginForm class to present the form to the user
from .forms import LoginForm
# импорт декоратора для отображения части веб-сайта для авторизированых пользователей
# import a decorator to display a portion of the website for logged in users
from django.contrib.auth.decorators import login_required


# определение функции user_login, которая получает запрос POST or GET и отправляющая ответ
# defining a user_login function that receives a POST or GET request and sends a response
def user_login(request):
    # проверка запроса
    # check request
    if request.method == 'POST': 
        form = LoginForm(request.POST)  # определение формы; defining the form
        # проверка формы на валидность
        # check the form for validity
        if form.is_valid():
            # получение валидных данных из формы
            # getting valid data from the form 
            cd = form.cleaned_data  # метод cleaned_data позволяет получить данные валидной формы; the cleaned_data method allows you to get the data of a valid form
            # поиск пользователя в базе данных с помощью метода authenticate
            # search for a user in the database using the authenticate method
            user = authenticate(username=cd['username'], password=cd['password'])
            # проверка на регистрацию и статус пользователя + отправка ответа
            # check for user registration and status of a user  + send a response
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        # если был получен запрос, например, GET, то пользователю отправляется пустая форма для заполнения
        # if a request was received, for example, GET, then an empty form is sent to the user to fill out
        form = LoginForm()
    # отправка ответа пользователю
    # send a response to the user
    return render(request, 'account/login.html', {'form': form})


# декотратор для проверки авторизации пользователя
# decorator for checking user authorization
@login_required 
def profile(request):
    return render(request, 'account/profile.html', {'section': 'profile'})


# метод для представления формы при регистрации пользователя
# method for submitting a form when registering a user
def register(request):
    # проверка на запрос пользователя
    # check for user request
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        # проверка на валидность формы
        # check for the validity of the form
        if user_form.is_valid():
            # создание нового пользователя, но предварительно не сохраняя его в базе данных
            # creating a new user, but without first saving it in the database
            new_user = user_form.save(commit=False)
            # установка пароля пользователю
            # setting a password to the user
            new_user.set_password(user_form.cleaned_data['password'])
            # окончательное сохранение данных о пользователе в базе данных
            # final saving of user data in the database
            new_user.save()
            # создание профиля для пользователя
            # creating a profile for a user
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# метод для представления формы редактирования информации о пользователе
# method for submitting a form when editing user information
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
