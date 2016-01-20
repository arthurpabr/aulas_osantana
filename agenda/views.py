# _*_ encoding: utf-8 _*_
from django.shortcuts import render, redirect
from agenda.models import ItemAgenda
from agenda.forms import ItemAgendaForm
from django.contrib.auth.decorators import login_required

@login_required
def lista(request):
	lista_de_itens = ItemAgenda.objects.filter(usuario=request.user)
	return render(request, 'lista.html', {"lista_de_itens": lista_de_itens})

@login_required
def adiciona(request):
	form = ItemAgendaForm()
	if request.method == 'POST':
		form = ItemAgendaForm(request.POST)
		if form.is_valid():
			#dados = form.cleaned_data
			#item = ItemAgenda(
			#	data = dados['data'],
			#	hora = dados['hora'],
			#	titulo = dados['titulo'],
			#	descricao = dados['descricao']
			#)
			#item.save()
			item = form.save(commit=False)
			item.usuario = request.user
			item.save()
			return render(request,'salvo.html',{})		
	return render(request, 'adiciona.html', {"form": form})

@login_required
def item(request, nr_item):
	#consultar 20min do vídeo 11
	pass

@login_required
def remove(request):
	#consultar 20min do vídeo 11
	pass