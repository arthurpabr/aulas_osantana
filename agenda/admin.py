from django.contrib import admin
from agenda.models import ItemAgenda

class ItemAgendaAdmin(admin.ModelAdmin):
	fields = ('titulo', 'data', 'hora', 'descricao', 'participantes')
	list_display = ('data', 'hora', 'titulo')

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

	def get_queryset(self, request):
		qs = super(ItemAgendaAdmin, self).get_queryset(request)
		return qs.filter(usuario=request.user)

admin.site.register(ItemAgenda, ItemAgendaAdmin)