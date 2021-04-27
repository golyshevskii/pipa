from django.forms import forms
from .models import ProfileBoard


class CreateBoard(forms.Form):
    class Meta:
        model = ProfileBoard
        field = ('title', 'image', 'url', 'content')


class EditBoard(forms.Form):
    class Meta:
        model = ProfileBoard
        field = ('title', 'image', 'url', 'content')
