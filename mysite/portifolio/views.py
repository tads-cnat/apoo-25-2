from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Aluno

class AdicaoUsuarioView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'portifolio/form_usuario.html')
    
    def post(self, request, *args, **kwargs):
        login = request.POST.get('login', '')
        email = request.POST.get('email', '')
        senha1 = request.POST.get('senha1', '')
        senha2 = request.POST.get('senha2', '')
        matricula = request.POST.get('matricula', '')
        periodo = request.POST.get('periodo', '')
        if senha1 == senha2:
            if login and senha1 and email and matricula and periodo:
                usr = User.objects.create_user(login, email, senha1)
                aluno = Aluno(user=usr, matricula=matricula, periodo=periodo)
                aluno.save()
                return render(request, 'portifolio/login.html')