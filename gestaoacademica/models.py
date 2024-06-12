from django.db import models
from django.conf import settings
import datetime


class Aluno(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.TextField(verbose_name="Nome do Aluno")
    sobrenome = models.TextField(verbose_name="Sobrenome do Aluno")
    prontuario = models.TextField(
        db_index=True, unique=True, default="AP", verbose_name="Registro do Aluno"
    )

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Aluno da Insituição"

    def __str__(self):
        return f"Aluno: {self.nome} {self.sobrenome}"

class Professor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.TextField()
class Turma(models.Model):
    aluno = models.ManyToManyField(Aluno)
    nome = models.TextField()

class Sala(models.Model):
    idSala = models.TextField(unique=True, db_index=True)
    capacidade = models.IntegerField(default=0)

class Disciplina(models.Model):
    nome = models.TextField(name="Nome da disciplina", default="")
    dependencia = models.ForeignKey('self', on_delete = models.SET_NULL,null=True)    
    cargaHoraria = models.IntegerField(default=0)



class OfertaDisciplina(models.Model):
    DIAS_DA_SEMANA = [
        ("DOMINGO", "Domingo"),
        ("SEGUNDA", "Segunda-feira"),
        ("TERCA", "Terça-feira"),
        ("QUARTA", "Quarta-feira"),
        ("QUINTA", "Quinta-feira"),
        ("SEXTA", "Sexta-feira"),
        ("SABADO", "Sábado"),
    ]
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE,null=True)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE,null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,null=True)
    diaDaSemana = models.TextField(choices=DIAS_DA_SEMANA, default="DOMINGO")
    sala = models.ForeignKey(Sala, null=True, on_delete=models.SET_NULL) 
    horarioInicio = models.TimeField(default=datetime.datetime.now().time())
    horarioFim = models.TimeField(default=datetime.datetime.now().time())

class Participacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    ofertaDisciplina = models.ForeignKey(OfertaDisciplina,on_delete=models.CASCADE, null=True)