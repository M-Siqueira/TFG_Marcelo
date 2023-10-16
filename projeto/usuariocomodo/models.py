import json

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
        ('MEDIA', 'Média' ),
        ('FRACA', 'Fraco' ),
        ('DESLIGADA', 'Desligada' ),
    )  

    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    CLIMATIZACAO = (
        ('ALTA', 'Alta'),
        ('MEDIA', 'Média' ),
        ('BAIXA', 'Baixa' ),
        ('DESLIGADA', 'Desligada' ),
    )  
    
    usuario = models.ForeignKey('usuario.Usuario', verbose_name= 'Usuário ou pessoa para cômodo *', on_delete=models.PROTECT, related_name='usuario')
    comodo = models.ForeignKey('comodo.Comodo', verbose_name= 'Cômodo associado a este usuário *', on_delete=models.PROTECT, related_name='comodo')
    prioridade = models.CharField('Usuário tem prioridade neste cômodo *', max_length=3, choices=PRIORIDADE, help_text='* Campos obrigatórios')
    crenca_webservice = models.TextField('Base de crença convertida do banco para AgentSpeak(L) e Jason', max_length=1000, null=True, blank=True)
    json_webservice = models.TextField('Base JSON convertida do banco', max_length=1000, null=True, blank=True)
        
    verao_iluminacao_manha = models.CharField('Manhã: ', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    verao_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    verao_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    inverno_iluminacao_manha = models.CharField('Manhã', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    inverno_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    inverno_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    primavera_iluminacao_manha = models.CharField('Manhã', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    primavera_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    primavera_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    outono_iluminacao_manha = models.CharField('Manhã', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    outono_iluminacao_tarde = models.CharField('Tarde', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')
    outono_iluminacao_noite = models.CharField('Noite', max_length=10, choices=ESTAGIO, default='DESLIGADA', null=True, blank=True, help_text='Itensidade da iluminação')

    verao_climatizacao_manha = models.CharField('Manhã: ', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    verao_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    verao_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    inverno_climatizacao_manha = models.CharField('Manhã', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    inverno_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    inverno_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    primavera_climatizacao_manha = models.CharField('Manhã', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    primavera_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    primavera_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    outono_climatizacao_manha = models.CharField('Manhã', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    outono_climatizacao_tarde = models.CharField('Tarde', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
    outono_climatizacao_noite = models.CharField('Noite', max_length=10, choices=CLIMATIZACAO, default="MEDIA", null=True, blank=True, help_text='Baixa: menos de 20 graus; Alta: acima de 24 graus')
                                               
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

    def gerar_json_webservice(self):

        crenca_iluminacao = {
            "servico"   : "iluminacao",
            "cidade"    : self.comodo.cidade,
            "lugar"     : self.comodo.lugar,
            "descricao" : self.comodo.descricao,
            "usuario"   : self.usuario.nome,
            "primavera_manha"   : self.primavera_iluminacao_manha,
            "primavera_tarde"   : self.primavera_iluminacao_tarde,
            "primavera_noite"   : self.primavera_iluminacao_noite,
            "verao_manha"   : self.verao_iluminacao_manha,
            "verao_tarde"   : self.verao_iluminacao_tarde,
            "verao_noite"   : self.verao_iluminacao_noite,
            "outono_manha"   : self.outono_iluminacao_manha,
            "outono_tarde"   : self.outono_iluminacao_tarde,
            "outono_noite"   : self.outono_iluminacao_noite,
            "inverno_manha"   : self.inverno_iluminacao_manha,
            "inverno_tarde"   : self.inverno_iluminacao_tarde,
            "inverno_noite"   : self.inverno_iluminacao_noite,
        }

        crenca_climatizacao = {
            "servico"   : "climatizacao",
            "cidade"    : self.comodo.cidade,
            "lugar"     : self.comodo.lugar,
            "descricao" : self.comodo.descricao,
            "usuario"   : self.usuario.nome,
            "primavera_manha"   : self.primavera_climatizacao_manha,
            "primavera_tarde"   : self.primavera_climatizacao_tarde,
            "primavera_noite"   : self.primavera_climatizacao_noite,
            "verao_manha"   : self.verao_climatizacao_manha,
            "verao_tarde"   : self.verao_climatizacao_tarde,
            "verao_noite"   : self.verao_climatizacao_noite,
            "outono_manha"   : self.outono_climatizacao_manha,
            "outono_tarde"   : self.outono_climatizacao_tarde,
            "outono_noite"   : self.outono_climatizacao_noite,
            "inverno_manha"   : self.inverno_climatizacao_manha,
            "inverno_tarde"   : self.inverno_climatizacao_tarde,
            "inverno_noite"   : self.inverno_climatizacao_noite,
        }

        json_crenca_iluminacao = json.dumps(crenca_iluminacao, indent=4)
        json_crenca_climatizacao = json.dumps(crenca_climatizacao, indent=4)
        return json_crenca_iluminacao + "\n\n" + json_crenca_climatizacao

    def gerar_crenca_webservice(self):
        vetor_cidade = self.comodo.cidade.lower().split(" ")
        if len(vetor_cidade) > 1:
            cidade = vetor_cidade[0] + "_" + vetor_cidade[-1]
        else:
            cidade = vetor_cidade[0]

        vetor_lugar = self.comodo.lugar.lower().split(" ")
        if len(vetor_lugar) > 1:
            lugar = vetor_lugar[0] + "_" + vetor_lugar[-1]
        else:
            lugar = vetor_lugar[0]

        vetor_descricao = self.comodo.descricao.lower().split(" ")
        if len(vetor_descricao) > 1:
            descricao = vetor_descricao[0] + "_" + vetor_descricao[-1]
        else:
            descricao = vetor_descricao[0]

        usuario = str(self.usuario.get_primeiro_nome.lower()) + '_' + str(self.usuario.get_sobrenome.lower())

        crenca = ''
        #iluminacao nas 4 estacoes
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',primavera,manha,'+self.primavera_iluminacao_manha.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',primavera,tarde,'+self.primavera_iluminacao_tarde.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',primavera,noite,'+self.primavera_iluminacao_noite.lower() + ').\n'

        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',verao,manha,'+self.verao_iluminacao_manha.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',verao,tarde,'+self.verao_iluminacao_tarde.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',verao,noite,'+self.verao_iluminacao_noite.lower() + ').\n'
        
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',outono,manha,'+self.outono_iluminacao_manha.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',outono,tarde,'+self.outono_iluminacao_tarde.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',outono,noite,'+self.outono_iluminacao_noite.lower() + ').\n'

        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',inverno,manha,'+self.inverno_iluminacao_manha.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',inverno,tarde,'+self.inverno_iluminacao_tarde.lower() + ').\n'
        crenca += 'iluminacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',inverno,noite,'+self.inverno_iluminacao_noite.lower() + ').\n'

        #climatizacao nas 4 estacoes
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',primavera,manha,'+self.primavera_climatizacao_manha.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',primavera,tarde,'+self.primavera_climatizacao_tarde.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',primavera,noite,'+self.primavera_climatizacao_noite.lower() + ').\n'

        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',verao,manha,'+self.verao_climatizacao_manha.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',verao,tarde,'+self.verao_climatizacao_tarde.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',verao,noite,'+self.verao_climatizacao_noite.lower() + ').\n'
        
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',outono,manha,'+self.outono_climatizacao_manha.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',outono,tarde,'+self.outono_climatizacao_tarde.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',outono,noite,'+self.outono_climatizacao_noite.lower() + ').\n'

        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',inverno,manha,'+self.inverno_climatizacao_manha.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',inverno,tarde,'+self.inverno_climatizacao_tarde.lower() + ').\n'
        crenca += 'climatizacao_' + cidade + '_' + lugar + '_' + descricao + '(' + usuario + ',inverno,noite,'+self.inverno_climatizacao_noite.lower() + ').\n'

        return crenca


    def save(self, *args, **kwargs):   
        self.crenca_webservice = self.gerar_crenca_webservice()      
        self.json_webservice = self.gerar_json_webservice()  

        super(UsuarioComodo, self).save(*args, **kwargs)
         
    @property
    def get_absolute_url(self):
        return reverse('usuariocomodo_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('usuariocomodo_delete', args=[str(self.id)])
    
    @property
    def get_visualiza_url(self):
        return reverse('usuariocomodo_detail', args=[str(self.id)])
    
    @property
    def get_visualiza_json_url(self):
        return reverse('usuariocomodo_json_detail', args=[str(self.id)])

