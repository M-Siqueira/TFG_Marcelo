from __future__ import unicode_literals
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from typing import Any

from rele.models import Rele
from .forms import BuscaReleForm

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin


class ReleListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Rele
    success_url = 'rele_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaReleForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaReleForm()
        return context

    def get_queryset(self):
        qs = Rele.objects.all()
        
        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaReleForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaReleForm()

        if form.is_valid():
            pesquisa = form.cleaned_data.get('pesquisa')

            if pesquisa:
                qs = qs.filter(Q(descricao__icontains=pesquisa)|Q(marca__icontains=pesquisa)|Q(modelo__icontains=pesquisa))
            
        return qs


class ReleCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Rele
    fields = ['descricao','marca', 'modelo', 'ip', 'porta_logica', 'is_active']
    success_url = 'rele_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Relé cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)

class ReleUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Rele
    fields = ['descricao','marca', 'modelo', 'ip', 'porta_logica', 'is_active']
    success_url = 'rele_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do Relé atualizados com sucesso na plataforma!')
        return reverse(self.success_url) 


class ReleDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Rele
    success_url = 'rele_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse Relé, permissão negada!')
        return redirect(self.success_url)
    
    
