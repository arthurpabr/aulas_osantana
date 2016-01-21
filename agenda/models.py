# _*_ encoding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User

class ItemAgenda(models.Model):
	data = models.DateField()
	hora = models.TimeField()		
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	usuario = models.ForeignKey(User)
	participantes = models.ManyToManyField(User, related_name="item_participantes")

	#o método abaixo personaliza o nome do objeto dentro do ambiente 'admin'
	def __unicode__(self):
		return u"%s - %s %s" % (self.titulo, self.data, self.hora)