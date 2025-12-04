from django.db import models
from django.contrib.auth.models import User

## ALUNO
########
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField('matrícula')
    periodo = models.CharField('período', max_length=5)
    def __str__(self):
        return 'Aluno: {}'.format(self.matricula)

## VAGA
#######
class Vaga(models.Model):
    titulo = models.CharField('título', max_length=100)
    descricao = models.TextField('descrição')
    requisitos = models.TextField()
    remuneracao = models.DecimalField('remuneração', max_digits=15, decimal_places=2)
    data_postagem = models.DateField()
    data_final = models.DateField()
    # relacionamento com rótulos
    # relacionamento com empresa
    def __str__(self):
        return self.titulo

## COMENTARIO
#############
class Comentario(models.Model):
    texto = models.CharField(max_length=100)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    def __str__(self):
        return self.texto