from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# представление шаблона chatroom пользователю
@login_required
def chat(request):
    return render(request, 'chat/chatroom.html')
