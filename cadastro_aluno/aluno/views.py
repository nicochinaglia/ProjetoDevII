from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from aluno.models import Aluno

class AlunoList(ListView):
    model = Aluno

class AlunoView(DetailView):
    model = Aluno

class AlunoCreate(CreateView):
    model = Aluno
    fields = ['name', 'fatec', 'ra']
    success_url = reverse_lazy('aluno_list')

class AlunoUpdate(UpdateView):
    model = Aluno
    fields = ['name', 'fatec', 'ra']
    success_url = reverse_lazy('aluno_list')

class AlunoDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno_list')
