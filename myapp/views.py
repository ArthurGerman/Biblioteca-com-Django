from django.shortcuts import render


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor, Livro


# ── AUTOR ───────────────────────────────────────────
class AutorListView(ListView):
    model = Autor
    template_name = 'myapp/autor_list.html'
    context_object_name = 'autores'

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'myapp/autor_detail.html'

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nome', 'email']
    template_name = 'myapp/autor_form.html'
    success_url = reverse_lazy('autor-list')

class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nome', 'email']
    template_name = 'myapp/autor_form.html'
    success_url = reverse_lazy('autor-list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'myapp/autor_confirm_delete.html'
    success_url = reverse_lazy('autor-list')


# ── LIVRO ───────────────────────────────────────────
class LivroListView(ListView):
    model = Livro
    template_name = 'myapp/livro_list.html'
    context_object_name = 'livros'

class LivroCreateView(CreateView):
    model = Livro
    fields = ['titulo', 'autor', 'ano_publicacao']
    template_name = 'myapp/livro_form.html'
    success_url = reverse_lazy('livro-list')

class LivroUpdateView(UpdateView):
    model = Livro
    fields = ['titulo', 'autor', 'ano_publicacao']
    template_name = 'myapp/livro_form.html'
    success_url = reverse_lazy('livro-list')

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'myapp/livro_detail.html'

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'myapp/livro_confirm_delete.html'
    success_url = reverse_lazy('livro-list')
