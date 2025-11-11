from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField('matrícula')
    periodo = models.CharField('período', max_length=5)
    def __str__(self):
        return 'Aluno: {}'.format(self.matricula)
