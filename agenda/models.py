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

def envia_email(**kwargs):
	try:
		item = kwargs['instance']
	except KeyError:
		return

	for participante in item.participantes.all():
		if not participante.email:
			continue

		dados = (item.titulo, item.data.strftime("%d/%m/%Y"), item.hora)
		participante.email_user(
				subject="[evento] %s dia %s as %s" % dados,
				message="Evento: %s\nDia: %s\nHora: %s\n" % dados,
				from_email=item.usuario.email
			)

models.signals.post_save.connect(envia_email, sender=ItemAgenda,
 dispatch_uid="agenda.models.ItemAgenda")