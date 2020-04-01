from django.db import models
from django.utils import timezone

class News(models.Model):
    author = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.author

class SportNews(models.Model):
    author = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.author
