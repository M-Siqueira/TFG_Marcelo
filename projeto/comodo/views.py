from __future__ import unicode_literals
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from typing import Any

from comodo.models import Comodo
from .forms import BuscaComodoForm

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin


class ComodoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Comodo
    success_url = 'comodo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaComodoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaComodoForm()
        return context

    def get_queryset(self):
        qs = Comodo.objects.all()
        
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaComodoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaComodoForm()

        if form.is_valid():
            pesquisa = form.cleaned_data.get('pesquisa')

            if pesquisa:
                qs = qs.filter(Q(descricao__icontains=pesquisa)|Q(equipamentos__descricao__icontains=pesquisa))
            
        return qs


class ComodoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Comodo
    fields = ['descricao', 'lugar', 'cidade', 'equipamentos', 'is_active']
    success_url = 'comodo_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Cômodo cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)

class ComodoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Comodo
    fields = ['descricao', 'lugar', 'cidade', 'equipamentos', 'is_active']
    success_url = 'comodo_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do Cômodo atualizados com sucesso na plataforma!')
        return reverse(self.success_url) 


class ComodoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Comodo
    success_url = 'comodo_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse Cômodo, permissão negada!')
        return redirect(self.success_url)
    
    
