# _*_ encoding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse(u"Olá mundo")