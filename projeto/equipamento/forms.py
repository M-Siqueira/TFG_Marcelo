from django import forms

  
class BuscaEquipamentoForm(forms.Form):
    pesquisa = forms.CharField(label='Digite algo para pesquisar', required=False)
    