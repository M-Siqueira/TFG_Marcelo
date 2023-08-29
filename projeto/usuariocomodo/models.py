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
    prioridade = models.CharField('Usuário tem prioridade neste cômodo *', max_length=3, choices=PRIORIDADE, help_text='* Campos obrigatórios')
    # verao_temperatura_manha
    # verao_temperatura_tarde
    # verao_temperatura_noite
    # inverno_temperatura_manha
    # inverno_temperatura_tarde
    # inverno_temperatura_noite
    # primavera_temperatura_manha
    # primavera_temperatura_tarde
    # primavera_temperatura_noite
    # outono_temperatura_manha
    # outono_temperatura_tarde
    # outono_temperatura_noite
    is_active = models.BooleanField('Ativo', default=True)
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    objects = models.Manager()

    class Meta:
        ordering            =   ['-is_active','usuario', 'comodo']
        unique_together     =  [['usuario', 'comodo']]
        verbose_name        =   'UsuarioComodo'
        verbose_name_plural =   'UsuarioComodos' 

    
    def __str__(self):
        return '%s - %s' % (self.usuario.nome, self.comodo.descricao)

    def save(self, *args, **kwargs):        
        super(UsuarioComodo, self).save(*args, **kwargs)
         
    @property
    def get_absolute_url(self):
        return reverse('usuariocomodo_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('usuariocomodo_delete', args=[str(self.id)])

