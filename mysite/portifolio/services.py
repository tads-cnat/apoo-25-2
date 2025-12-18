from abc import ABC, abstractmethod
from django.contrib.auth.models import User
from .models import Aluno, Vaga, Comentario
from django.db.models import Q

## VagaService
##############
class VagaService:
    def get_vaga(self, id_vaga):
        try:
            obj = Vaga.objects.get(pk=id_vaga)
            return obj
        except(Vaga.DoesNotExist):
            return None
    def pesquisa_vaga(self, termo):
        vagas = Vaga.objects.filter(Q(titulo__icontains=termo) | Q(descricao__icontains=termo))
        return vagas

## ComentarioService
####################
class ComentarioService:
    def comentar_vaga(self, usuario, id_vaga, texto):
        srv = VagaService()
        vaga = srv.get_vaga(id_vaga)
        if vaga and usuario.is_authenticated and hasattr(usuario, 'aluno'):
            coment = Comentario(texto=texto, aluno=usuario.aluno, vaga=vaga)
            coment.save()
            return {'sucesso': 'Comentário registrado com sucesso.'}
        return {'erro': 'Identicação de vaga ou usuário inválidos!'}

## ComentarVagaService
######################
class ComentarVagaService(ABC):
    @staticmethod
    def get_instancia():
        return ComentarVagaImpl1()
    @abstractmethod
    def get_vaga(self, id_vaga):
        pass

## ComentarVagaImpl1
####################
class ComentarVagaImpl1(ComentarVagaService):
    def get_vaga(self, id_vaga):
        try:
            obj = Vaga.objects.get(pk=id_vaga)
            return obj
        except(Vaga.DoesNotExist):
            return None


## UsuarioService
#################
class UsuarioService:
    def cadastrar_usuario(self, mapa):
        if self.validar(mapa):
            usr = User.objects.create_user(
                mapa['login'], mapa['email'], mapa['senha1']
            )
            aluno = Aluno(
                user=usr, matricula=mapa['matricula'], 
                periodo=mapa['periodo']
            )
            aluno.save()
            return {'sucesso': 'Usuário cadastrado com sucesso!'}
        elif self.senhas_diferentes(mapa):
            return {'erro': 'Senhas precisam ser iguais!'}
        return {'erro': 'Todos os parâmetros devem ser informados!'}

    def validar(self, mapa):
        if (mapa['login'] and mapa['senha1'] and mapa['senha2'] and
            mapa['email'] and mapa['periodo'] and mapa['matricula']):
            if mapa['senha1'] == mapa['senha2']:
                return True
        return False

    def senhas_diferentes(self, mapa):
        return not mapa['senha1'] == mapa['senha2']