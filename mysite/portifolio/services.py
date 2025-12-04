from django.contrib.auth.models import User
from .models import Aluno, Vaga, Comentario

## VagaService
##############
class VagaService:
    def get_vaga(self, id_vaga):
        try:
            obj = Vaga.objects.get(pk=id_vaga)
            return obj
        except(Vaga.DoesNotExist):
            return None

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