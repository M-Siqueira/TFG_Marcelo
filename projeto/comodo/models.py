from django.db import models
from django.urls import reverse


class Comodo(models.Model):
    descricao = models.CharField('Descrição do cômodo', max_length=50, help_text="Quarto do pai ou Sala de estar.")
    equipamentos = models.ManyToManyField('equipamento.Equipamento', verbose_name='Equipamento(s)', null=True, blank=True, related_name='equipamentos', help_text='Para selecionar ou deselecionar um equipamento pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    is_active = models.BooleanField('Ativo', default=True)
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    objects = models.Manager()

    class Meta:
        ordering            =   ['-is_active','descricao']
        verbose_name        =   'comodo'
        verbose_name_plural =   'comodos'

    
    def __str__(self):
        return '%s' % (self.descricao)

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        super(Comodo, self).save(*args, **kwargs)
         
    @property
    def get_absolute_url(self):
        return reverse('comodo_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('comodo_delete', args=[str(self.id)])

