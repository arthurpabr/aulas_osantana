# _*_ encoding: utf-8 _*_
from django.shortcuts import render, redirect
from agenda.models import ItemAgenda
from agenda.forms import ItemAgendaForm

def lista(request):
	lista_de_itens = ItemAgenda.objects.all()
	return render(request, 'lista.html', {"lista_de_itens": lista_de_itens})

def adiciona(request):
	form = ItemAgendaForm()
	if request.method == 'POST':
		form = ItemAgendaForm(request.POST)
		if form.is_valid():
			dados = form.cleaned_data
			item = ItemAgenda(
				data = dados['data'],
				hora = dados['hora'],
				titulo = dados['titulo'],
				descricao = dados['descricao']
			)
			item.save()
			return render(request,'salvo.html',{})		
	return render(request, 'adiciona.html', {"form": form})

	def detalha(request):
		pass