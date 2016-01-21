# _*_ encoding: utf-8 _*_
from django.shortcuts import render, redirect, get_object_or_404
from agenda.models import ItemAgenda
from agenda.forms import ItemAgendaForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

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
	#try:
	#	item = ItemAgenda.objects.get(id=nr_item)
	#except ItemAgenda.DoesNotExist:
	#	raise Http404(u"Este item não existe!")
	item = get_object_or_404(ItemAgenda, pk=nr_item, usuario=request.user)
	if request.method == 'POST':
		form = ItemAgendaForm(request.POST, instance=item)
		if form.is_valid:
			form.save()
			return render(request,'salvo.html',{})	
	else :
		form = ItemAgendaForm(instance=item)
	return render(request, 'item.html', {"form": form})	

@login_required
def remove(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item)
	if request.method == 'POST':
		item.delete()
		return render(request,'removido.html',{})	

	return render(request, 'remove.html', {"item": item})	