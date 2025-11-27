from django.shortcuts import render
from django.views import View
from .services import UsuarioService

class AdicaoUsuarioView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'portifolio/form_usuario.html')
    
    def post(self, request, *args, **kwargs):
        param = self.extrai_parametros(request)
        srv = UsuarioService()
        retorno = srv.cadastrar_usuario(param)
        if 'erro' in retorno:
            return render(request,'portifolio/form_usuario.html', retorno)
        return render(request, 'portifolio/login.html', retorno)
    
    def extrai_parametros(self, request):
        login = request.POST.get('login', '')
        email = request.POST.get('email', '')
        senha1 = request.POST.get('senha1', '')
        senha2 = request.POST.get('senha2', '')
        matricula = request.POST.get('matricula', '')
        periodo = request.POST.get('periodo', '')
        param = {
            'login': login,
            'email': email,
            'senha1': senha1,
            'senha2': senha2,
            'matricula': matricula,
            'periodo': periodo,
        }
        return param
