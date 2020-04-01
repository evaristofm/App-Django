from django.db import models

class News(models.Model):
    author = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.author

class SportNews(models.Model):
    author = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.author
