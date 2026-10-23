from django.db import models

class Conteudo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    conteudo_html = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Menu(models.Model):
    TIPO_CHOICES = (
        ('interno', 'Interno'),
        ('externo', 'Externo'),
    )

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    
    # Relacionamento opcional para link interno:
    conteudo = models.ForeignKey(
        Conteudo, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    
    # Campo opcional para link externo:
    url_externa = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo

