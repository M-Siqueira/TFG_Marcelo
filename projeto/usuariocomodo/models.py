from django.db import models
from django.urls import reverse


class UsuarioComodo(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    PRIORIDADE = (
        ('SIM', 'Sim'),
        ('NÃO', 'Não' ),
    )   
    usuario = models.ForeignKey('usuario.Usuario', verbose_name= 'Usuário ou pessoa para cômodo *', on_delete=models.PROTECT, related_name='usuario')
    comodo = models.ForeignKey('comodo.Comodo', verbose_name= 'Cômodo associado a este usuário *', on_delete=models.PROTECT, related_name='comodo')
    lugar = models.CharField('Localização deste cômodo *', max_length=30, null=True, blank=False,  help_text='Por exemplo, Casa da Praia ou Escritório ou Apartamento na Praia')
    prioridade = models.CharField('Usuário tem prioridade neste cômodo *', max_length=3, choices=PRIORIDADE, help_text='* Campos obrigatórios')
    is_active = models.BooleanField('Ativo', default=True)
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    objects = models.Manager()

    class Meta:
        ordering            =   ['-is_active','usuario', 'comodo']
        unique_together     =  [['usuario', 'comodo', 'lugar']]
        verbose_name        =   'UsuarioComodo'
        verbose_name_plural =   'UsuarioComodos' 

    
    def __str__(self):
        return '%s - %s' % (self.usuario.nome, self.comodo.descricao)

    def save(self, *args, **kwargs):        
        self.lugar = self.lugar.upper()
        super(UsuarioComodo, self).save(*args, **kwargs)
         
    @property
    def get_absolute_url(self):
        return reverse('usuariocomodo_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('usuariocomodo_delete', args=[str(self.id)])

