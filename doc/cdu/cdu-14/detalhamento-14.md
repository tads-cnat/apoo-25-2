# CDU 14. Enviar mensagem em chat específico 

- **Ator principal**: Usuário (logado)
- **Atores secundários**: não possui.
- **Resumo**: ao estar visualizando um chat específico, contendo as mensagens trocadas com outro usuário, o usuário em questão digita e envia uma nova mensagem.
- **Pré-condição**: estar visualizando um chat específico.
- **Pós-Condição**: uma nova mensagem é adicionada ao chat específico.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - visualizando um chat específico com um outro usuário, o usuário decide enviar uma nova mensagem | |  
| | 1 - no final do chat é exibido um formulário para receber uma nova mensagem e um botão para a submissão |
| 2 - o usuário digita a nova mensagem e submete o formulário | |
| | 3 - o sistema torna a exibir o chat, incluindo a mensagem recém postada | 

## Fluxo Alternativo I - Submissão sem texto
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 3.1 - o sistema torna a exibir o chat com uma mensagem de erro indicando mensagem inválida |
| (fluxo finalizado) | |

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...