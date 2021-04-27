from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# представление шаблона chatroom пользователю
# presenting the chatroom template to the user
@login_required
def chat(request):
    return render(request, 'chat/chatroom.html')
