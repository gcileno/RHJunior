from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ej.models import Voluntario
from certificados.models import Certificados

from scripts import certificado

def login_view(request):
    return render(request, 'login.html')

def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('portal')
        else:
            messages.error(request,'Usuário ou senha inválidos.')        
    return redirect('login')
    
def logout_user(request):
    logout(request)
    return redirect('login')


@method_decorator(login_required(login_url='login'), name = 'dispatch')
class Portal_view(View):
    template_name = "portal.html"
    
    def get(self, request):
        voluntario = Voluntario.objects.get(user__id=request.user.id)
        certificados = Certificados.objects.filter(historico_membro__voluntario__user__id=request.user.id)

        context = {'voluntario': voluntario, 'certificados':certificados}

        
        return render(request, self.template_name, context)