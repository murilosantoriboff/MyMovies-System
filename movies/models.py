from django.db import models

class Filme(models.Model):
    choices_notas = (
        ('1', 'Muito Ruim'),
        ('2', 'Ruim'),
        ('3', 'Aceitavel'),
        ('4', 'Bom'),
        ('5', 'Muito Bom')
    )
    nome = models.CharField(max_length=100)
    sinopse = models.TextField()
    diretor = models.CharField(max_length=100)
    ano_lancamento = models.CharField(max_length=4)
    nota = models.CharField(choices=choices_notas, max_length=1)

    def __str__(self) -> str:
        return self.nome
