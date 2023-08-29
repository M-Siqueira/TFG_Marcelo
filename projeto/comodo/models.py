from django.db import models
from django.urls import reverse


class Comodo(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    LUGAR = (
        ('APARTAMENTO', 'Apartamento'),
        ('CASA', 'Casa'),
        ('CONSULTÓRIO', 'Consultório' ),
        ('ESCRITÓRIO', 'Escritório' ),
        ('SÍTIO', 'Sítio' ),
        ('OUTRO', 'Outro' ), 
    ) 
    descricao = models.CharField('Descrição do cômodo', max_length=50, help_text="Quarto do pai ou Sala de estar.")
    lugar = models.CharField('Localização deste cômodo *', max_length=12, choices=LUGAR, null=True, blank=False)
    cidade = models.CharField('Cidade *', max_length=30, null=True, blank=False)
    equipamentos = models.ManyToManyField('equipamento.Equipamento', verbose_name='Equipamento(s)', null=True, blank=True, related_name='equipamentos', help_text='Para selecionar ou deselecionar um equipamento pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    is_active = models.BooleanField('Ativo', default=True)
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    objects = models.Manager()

    class Meta:
        ordering            =   ['-is_active','descricao']
        unique_together     =  [['descricao', 'lugar', 'cidade']]
        verbose_name        =   'comodo'
        verbose_name_plural =   'comodos'

    
    def __str__(self):
        return '%s. %s - %s' % (self.descricao, self.lugar, self.cidade)

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        self.cidade = self.cidade.title()
        super(Comodo, self).save(*args, **kwargs)
         
    @property
    def get_absolute_url(self):
        return reverse('comodo_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('comodo_delete', args=[str(self.id)])

