# Orientação para Organização das Aplicações Web (Django)

A organização de uma aplicação Django utilizando uma camada de Services (também chamada de camada de aplicação) ajuda a separar a lógica de negócio complexa das views (controle) e dos models (domínio), seguindo princípios do **Domain-Driven Design (DDD)** ou **Clean Architecture**.

Abaixo está uma estrutura detalhada e exemplos práticos:

## 1. Estrutura do Projeto

```bash
meu_projeto/
├── meu_projeto/          # Configurações globais do projeto
├── usuarios/             # Aplicação de usuários (exemplo)
│   ├── models.py         # Classes de domínio
│   ├── views.py          # Classes de visão (Views - mínima lógica, só orquestração)
│   ├── services.py       # Classes de serviço com as implementações das regras de negócio 
│   ├── tests.py          # Classes de teste e seus respectivos métodos de teste
│   └── ...
│   pedidos/              # Aplicação de pedidos (exemplo)
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   └── ...
└── ...
├── requirements.txt
└── manage.py
```

## 2. Divisão de Responsabilidades
| Camada | O que faz? |	Exemplo de Código |
| ------ | ---------- | ----------------- |
| **Models** | Representam as entidades do domínio e implementam regras básicas. | **Produto**, **Pedido**, etc. |
| **Views** | Recebem as requisições e encaminham as respostas (lógica mínima). | **ListaProdutosView**, **AdicionaPedidoView**, etc. |
| **Services** | Contém a lógica de negócio complexa. | **ProdutoService**, **PedidoService**, etc. |


## 3. Implementação Detalhada

### (A) Models (Camada de Domínio)

Representam as entidades do domínio, as quais possuem a implementação das regras e validações básicas. Exemplos de classes de modelo: Pedido, Produto.

```python
# pedidos/models.py
from django.db import models

class Pedido(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Pedido #{self.id}"
```

### (B) Services (Camada de Aplicação)

Responsáveis pela implementação de lógica complexa da aplição, tais como:
- Criação de pedidos com validações.
- Cálculo de descontos.
- Integração com APIs externas (ex.: gateway de pagamento).

#### Exemplo 1: Service para Pedidos

```python
# pedidos/services.py
from .models import Pedido
from produtos.models import Produto

class PedidoService:
    _instancia = None

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia 

    def criar_pedido(usuario, produtos):
        """
        Cria um pedido com validações e regras de negócio.
        """
        if not produtos:
            raise ValueError("Nenhum produto selecionado.")

        pedido = Pedido.objects.create(usuario=usuario)
        for produto in produtos:
            if not produto.disponivel:
                raise ValueError(f"Produto {produto.nome} indisponível.")
            pedido.itens.add(produto)

        PedidoService._aplicar_desconto(pedido)
        return pedido

    def _aplicar_desconto(pedido):
        """Aplica desconto se o pedido for acima de R$ 100."""
        total = sum(item.preco for item in pedido.itens.all())
        if total > 100:
            pedido.desconto = 0.1 * total
            pedido.save()
```

#### Exemplo 2: Service para Usuários

```python
# usuarios/services.py
from django.contrib.auth import get_user_model

User = get_user_model()

class UsuarioService:
    _instancia = None

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def registrar_usuario(email, senha, nome):
        """Registra um usuário com validações."""
        if User.objects.filter(email=email).exists():
            raise ValueError("E-mail já cadastrado.")
        return User.objects.create_user(email=email, password=senha, nome=nome)
```

### (C) Views (Camada de Apresentação)

Responsabilidade:
- Receber requisições (*request*) HTTP.
- Chamar as classes de serviço para relizar a lógica da aplicação.
- Retornar respostas (normalmente HTML).

#### Exemplo: View Django

```python
# usuarios/views.py
from django.shortcuts import render, redirect
from django.views import View
from .services import UsuarioService

class RegistroUsuarioView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, "registro.html")

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        nome = request.POST.get("nome")
        try:
            srv = UsuarioService.get_instancia()
            usr = srv.registrar_usuario(email, senha, nome)
            return redirect("login")
        except ValueError as e:
            return render(request, "registro.html", {"erro": str(e)})
```

## 4. Vantagens Dessa Abordagem

✅ Separação clara de responsabilidades:
- Views cuidam apenas de HTTP.
- Services concentram regras de negócio.

✅ Testabilidade:
- Services podem ser testados isoladamente (sem depender de views).

✅ Reúso:
- Um mesmo service pode ser usado em:
- Views Django.
- Comandos manage.py.
- APIs REST (Django Rest Framework).
- Tarefas assíncronas (Celery).

✅ Manutenção mais fácil:
- Se uma regra de negócio muda, basta alterar o service, sem mexer em views ou models.