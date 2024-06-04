from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    hora_inicio = models.TimeField()
    data_final = models.DateField()
    hora_final = models.TimeField()
    local = models.CharField(max_length=255)
    criador = models.ForeignKey(max_length=255)

    def __str__(self):
        return self.titulo
