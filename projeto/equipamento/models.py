from django.db import models
from django.urls import reverse


class Equipamento(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPO = (
        ('CLIMATIZAÇÃO', 'Climatização'),
        ('ILUMINAÇÃO', 'Iluminação'),
    ) 
    descricao = models.CharField('Descrição do equipamento', max_length=40, help_text="Ar condicionado ou cafeteira ou sistema de iluminação.")
    marca = models.CharField('Marca', max_length=30)
    modelo = models.CharField('Modelo', max_length=30, null=True, blank=True, )
    tipo = models.CharField('Tipo do equipamento *', max_length=15, choices=TIPO, help_text='* Campos obrigatórios')
    observacao = models.CharField('Alguma observação ou detalhe do equipamento', null=True, blank=True, max_length=100)
    is_active = models.BooleanField('Ativo', default=True)
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    objects = models.Manager()

    class Meta:
        ordering            =   ['-is_active','descricao']
        verbose_name        =   'equipamento'
        verbose_name_plural =   'equipamentos'

    
    def __str__(self):
        return '%s. Tipo: %s. Marca: %s.'  % (self.descricao, self.tipo, self.marca)

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        self.marca = self.marca.upper()
        self.modelo = self.modelo.upper()
        super(Equipamento, self).save(*args, **kwargs)
         
    @property
    def get_absolute_url(self):
        return reverse('equipamento_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('equipamento_delete', args=[str(self.id)])

