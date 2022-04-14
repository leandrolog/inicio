from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Publishedmanager(models.Manager):
    def get_queryset(selfself):
        return super(PublishedManager,self).get_queryset()\
                                            .filter(status='publicado')

 #   STATUS = (
  #      ('rascunho', 'Rascunho'),
  #      ('publicado', 'Publicado'),
  #  )

class Post(models.Model):
    STATUS = (
         ('rascunho', 'Rascunho'),
         ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE, related_name='usuarios')
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)
    alterado  = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                                choices=STATUS,
                                 default='rascunho')

    class Meta:
        ordering = ('-publicado',)


    def __str__(self):
        return self.titulo

# Create your models here.
