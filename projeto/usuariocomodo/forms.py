from django import forms

  
class BuscaUsuarioComodoForm(forms.Form):
    pesquisa = forms.CharField(label='Digite algo para pesquisar', required=False)
    