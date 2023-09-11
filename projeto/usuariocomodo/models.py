from django.db import models
from django.urls import reverse


class UsuarioComodo(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    PRIORIDADE = (
        ('SIM', 'Sim'),
        ('NÃO', 'Não' ),
    )  

    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    ESTAGIO = (
        ('FORTE', 'Forte'),
        ('MÉDIA', 'Médio' ),
        ('FRACA', 'Fraco' ),
        ('DESLIGADA', 'Desligada' ),
    )  

    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    CLIMATIZACAO = (
        ('ALTA', 'Alta'),
        ('MÉDIA', 'Média' ),
        ('BAIXA', 'Baixa' ),
        ('DESLIGADA', 'Desligada' ),
    )  
    
    usuario = models.ForeignKey('usuario.Usuario', verbose_name= 'Usuário ou pessoa para cômodo *', on_delete=models.PROTECT, related_name='usuario')
    comodo = models.ForeignKey('comodo.Comodo', verbose_name= 'Cômodo associado a este usuário *', on_delete=models.PROTECT, related_name='comodo')
    prioridade = models.CharField('Usuário tem prioridade neste cômodo *', max_length=3, choices=PRIORIDADE, help_text='* Campos obrigatórios')
        
    verao_iluminacao_manha = models.CharField('Manhã: ', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    verao_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    verao_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    inverno_iluminacao_manha = models.CharField('Manhã', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    inverno_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    inverno_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    primavera_iluminacao_manha = models.CharField('Manhã', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    primavera_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    primavera_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    outono_iluminacao_manha = models.CharField('Manhã', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    outono_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')
    outono_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, null=True, blank=True, help_text='Itensidade da iluminação')

    verao_climatizacao_manha = models.CharField('Manhã: ', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    verao_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    verao_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    inverno_climatizacao_manha = models.CharField('Manhã', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    inverno_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    inverno_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    primavera_climatizacao_manha = models.CharField('Manhã', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    primavera_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    primavera_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    outono_climatizacao_manha = models.CharField('Manhã', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    outono_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    outono_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MÉDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
                                               
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

