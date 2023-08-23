from __future__ import unicode_literals
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from typing import Any

from equipamento.models import Equipamento
from .forms import BuscaEquipamentoForm

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin


class EquipamentoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Equipamento
    success_url = 'equipamento_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaEquipamentoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaEquipamentoForm()
        return context

    def get_queryset(self):
        qs = Equipamento.objects.all()
        
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaEquipamentoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaEquipamentoForm()

        if form.is_valid():
            pesquisa = form.cleaned_data.get('pesquisa')

            if pesquisa:
                qs = qs.filter(Q(descricao__icontains=pesquisa)|Q(marca__icontains=pesquisa)|Q(modelo__icontains=pesquisa)|Q(tipo__icontains=pesquisa))
            
        return qs


class EquipamentoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Equipamento
    fields = ['descricao','marca', 'modelo', 'tipo', 'observacao', 'is_active']
    success_url = 'equipamento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Equipamento cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)

class EquipamentoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Equipamento
    fields = ['descricao','marca', 'modelo', 'tipo', 'observacao', 'is_active']
    success_url = 'equipamento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do Equipamento atualizados com sucesso na plataforma!')
        return reverse(self.success_url) 


class EquipamentoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Equipamento
    success_url = 'equipamento_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse Equipamento, permissão negada!')
        return redirect(self.success_url)
    
    
