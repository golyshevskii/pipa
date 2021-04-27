# from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from board.models import ProfileBoard
from board.forms import CreateBoard, EditBoard
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BoardCreate(LoginRequiredMixin, CreateView):
    model = ProfileBoard
    template_name = 'board/board_create.html'
    form_class = CreateBoard
    success_url = reverse_lazy('board:profile_board')


class BoardEdit(LoginRequiredMixin, UpdateView):
    model = ProfileBoard
    template_name = 'board/board_edit.html'
    form_class = EditBoard
    success_url = reverse_lazy('board:profile_board')


class Board(LoginRequiredMixin, TemplateView):
    template_name = 'board/board.html'


class BoardDelete(LoginRequiredMixin, DeleteView):
    model = ProfileBoard
    template_name = 'board/board_delete.html'
    success_url = reverse_lazy('account:profile_board')
