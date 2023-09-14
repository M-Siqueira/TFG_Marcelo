from django.db import models
from django.urls import reverse


class Rele(models.Model):
     
    descricao = models.CharField('Descrição do relé', max_length=40, help_text="Acionador ou Sensor")
    marca = models.CharField('Marca', max_length=30)
    modelo = models.CharField('Modelo', max_length=30, null=True, blank=True)
    ip = models.GenericIPAddressField('Endereço IP do relé',max_length=15, help_text="Por exemplo, 192.168.10.3 ou 10.20.10.2")
    porta_logica = models.CharField('Porta lógica do relé',max_length=5, help_text="Por exemplo, 8081")
    is_active = models.BooleanField('Ativo', default=True)
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    objects = models.Manager()

    class Meta:
        ordering            =   ['-is_active', 'marca', 'descricao']
        verbose_name        =   'rele'
        verbose_name_plural =   'reles'

    
    def __str__(self):
        return '%s: %s'  % (self.marca, self.descricao)

    def save(self, *args, **kwargs):
        if self.descricao:
            self.descricao = self.descricao.upper()
        if self.marca:
            self.marca = self.marca.upper()
        if self.modelo:
            self.modelo = self.modelo.upper()
        super(Rele, self).save(*args, **kwargs)
         
    @property
    def get_absolute_url(self):
        return reverse('rele_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('rele_delete', args=[str(self.id)])

