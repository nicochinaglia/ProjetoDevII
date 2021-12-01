from django.db import models
from django.urls import reverse

class Aluno(models.Model):
    name = models.CharField(max_length=200)
    fatec = models.CharField(max_length=100)
    ra = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('aluno_edit', kwargs={'pk': self.pk})