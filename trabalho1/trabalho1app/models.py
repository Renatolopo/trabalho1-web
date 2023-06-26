from django.db import models

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    periodo_ingresso =  models.CharField('Período de Ingresso', max_length=100)
    nota = models.IntegerField('Nota')
    situacao = models.CharField('Situação', max_length=100, null=True, blank=True, editable=False)
    

    def save(self, *args, **kwargs):
        if self.nota >= 60:
            self.situacao = 'Aprovado'
        else:
            self.situacao = 'Reprovado'
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nome
