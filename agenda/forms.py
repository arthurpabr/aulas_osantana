from django import forms

#class ItemAgendaForm(forms.Form):
	#titulo = forms.CharField(max_length=100)
	#data = forms.DateField(
	#	widget=forms.DateInput(format='%d/%m/%Y'),
	#	input_formats=['%d/%m/%Y','%d/%m/%y'])
	#hora = forms.TimeField()		
	#descricao = forms.CharField()

from models import ItemAgenda

class ItemAgendaForm(forms.ModelForm):
	class Meta:
		model = ItemAgenda
		fields = ('titulo','data','hora','descricao')