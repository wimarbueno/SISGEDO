from principal.models import *
from principal.forms import RegisterUserCreateForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.forms import PerfilForm, EditarUserForm

def lista_usuarios(request):
	usuarios = User.objects.all()
	return render_to_response('usuarios.html', {'usuarios':usuarios}, context_instance=RequestContext(request))

def registrar_usuario(request):
	if request.method=='POST':
		formulario = RegisterUserCreateForm(request.POST)
		#Hay diferencia entre is_valid() y is_valid, mientras que el primero valida mostrando los errores el ultimo no muestra los errores.
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = RegisterUserCreateForm()
	return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

def editar_usuario(request, id_usuario):
	usuario = User.objects.get(pk = id_usuario)
	if request.method=='POST':
		formulario = EditarUserForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = EditarUserForm(instance = usuario)
	return render_to_response('editarusuario.html', {'formulario':formulario, 'usuario':usuario}, context_instance=RequestContext(request))

def ver_usuario(request, id_usuario):	
	dato = User.objects.get(pk=id_usuario)
	dato2 = PerfilUsuario.objects.filter(usuario=id_usuario)
	return render_to_response('ver_usuario.html',{'usuario':dato,'verPerfil':dato2},context_instance = RequestContext(request))

def ver_perfiles(request, id_usuario):	
	dato2 = PerfilUsuario.objects.filter(usuario=id_usuario)
	dato = User.objects.get(pk=id_usuario)
	return render_to_response('ver_perfiles.html',{'usuario':dato,'verPerfil':dato2},context_instance = RequestContext(request))

def nuevo_perfil(request, id_usuario):	
	dato = User.objects.get(pk=id_usuario)
	if request.method=='POST':
		formulario=PerfilForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else: 
		formulario=PerfilForm()
	return render_to_response('nuevoperfil.html',{'formulario':formulario, 'dato':dato}, context_instance=RequestContext(request))

