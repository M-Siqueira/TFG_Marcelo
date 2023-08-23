from django import forms

  
class BuscaComodoForm(forms.Form):
    pesquisa = forms.CharField(label='Digite algo para pesquisar', required=False)
    