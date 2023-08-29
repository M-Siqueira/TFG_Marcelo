from __future__ import unicode_literals
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from typing import Any

from usuariocomodo.models import UsuarioComodo
from .forms import BuscaUsuarioComodoForm

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin


class UsuarioComodoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = UsuarioComodo
    success_url = 'usuariocomodo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaUsuarioComodoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaUsuarioComodoForm()
        return context

    def get_queryset(self):
        qs = UsuarioComodo.objects.all()
        
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaUsuarioComodoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaUsuarioComodoForm()

        if form.is_valid():
            pesquisa = form.cleaned_data.get('pesquisa')

            if pesquisa:
                qs = qs.filter(Q(usuario__nome__icontains=pesquisa)|Q(comodo__descricao__icontains=pesquisa)|Q(lugar__icontains=pesquisa))
            
        return qs


class UsuarioComodoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = UsuarioComodo
    fields = ['usuario', 'comodo', 'prioridade', 'is_active']
    success_url = 'usuariocomodo_list'
    
    def get_success_url(self):
        messages.success(self.request, 'A relação de um Usuário a um Cômodo cadastrada com sucesso na plataforma!')
        return reverse(self.success_url)

class UsuarioComodoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = UsuarioComodo
    fields = ['usuario', 'comodo',  'prioridade', 'is_active']
    success_url = 'usuariocomodo_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados da relação entre Usuário e Cômodo atualizados com sucesso na plataforma!')
        return reverse(self.success_url) 


class UsuarioComodoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = UsuarioComodo
    success_url = 'usuariocomodo_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa relação de Usuário com Cômodo, permissão negada!')
        return redirect(self.success_url)
    