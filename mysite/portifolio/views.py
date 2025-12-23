from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .services import UsuarioService, VagaService, ComentarioService, ComentarVagaService

## DetalhaVagaView
##################
class DetalhaVagaView(View):
    def get(self, request, *args, **kwargs):
        id_vaga = kwargs['id_vaga']
        srv = VagaService()
        vaga = srv.get_vaga(id_vaga)
        if vaga:
            return render(request, 'portifolio/vaga_detalhes.html', {'vaga': vaga})
        messages.error(request, 'Identificador de Vaga inválido.')
        return redirect('index')


## PesquisaVagasView
####################
class PesquisaVagasView(View):
    def post(self, request, *args, **kwargs):
        termo = request.POST.get('texto', '')
        if len(termo) < 3:
            messages.error(request, 'O termo de pesquisa deve ter ao menos 3 caracteres.')
            return redirect('index')
        srv = VagaService()
        vagas = srv.pesquisa_vaga(termo)
        return render(request, 'portifolio/list_vaga.html', {'vagas': vagas, 'termo': termo})

## ComentarVagaView
###################
class ComentarVagaView(View):
    def get(self, request, *args, **kwargs):
        srv = ComentarVagaService.get_instancia()
        id_vaga = kwargs['id_vaga']
        vaga = srv.get_vaga(id_vaga)
        if vaga:
            return render(request, 'portifolio/form_comentario.html', {'vaga': vaga})
        messages.error(request, 'Vaga não encontrada.')
        return redirect('index')
    
    def post(self, request, *args, **kwargs):
        srv = ComentarVagaService.get_instancia()
        id_vaga = kwargs['id_vaga']
        texto = request.POST['texto']
        resultado = srv.add_comentario(request.user, id_vaga, texto)
        if 'sucesso' in resultado:
            messages.success(request, resultado['sucesso'])
            # TODO: 'detalhes_vaga' ainda não está implementado
            # por enquanto o resultado será redirecionado para a 'index'
            return redirect('index')
        messages.error(request, resultado['erro'])
        return redirect('index')

## AdicaoUsuarioView
####################
class AdicaoUsuarioView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'portifolio/form_usuario.html')
    
    def post(self, request, *args, **kwargs):
        param = self.extrai_parametros(request)
        srv = UsuarioService()
        retorno = srv.cadastrar_usuario(param)
        if 'erro' in retorno:
            messages.error(request, retorno['erro'])
            return render(request,'portifolio/form_usuario.html')
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('index')
    
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
