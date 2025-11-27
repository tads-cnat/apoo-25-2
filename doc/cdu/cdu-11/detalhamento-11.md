# CDU 11. Realiza auto-cadastro 

- **Ator principal**: Visitante.
- **Atores secundários**: não possui. 
- **Resumo**: Um usuário visitante, acessa a opção de realização do seu auto-cadastro, visualiza um formulário para preenchimento dos seus dados, preenche e submete. Após a validação dos dados o usuário é cadastrado no sistema.
- **Pré-condição**: Nenhuma.
- **Pós-Condição**: Objetos 'User' e 'Aluno' criados no armazenamento persistente.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - Usuário visitante aciona a opção de realização de auto-cadastro. | |  
| | 1 - Sistema apresenta um formulário com os dados que devem ser preenchidos (login, e-mail, senha, confirmação de senha, matrícula e período). |
| 2 - Usuário preenche e submete o formulário .| |
| | 3 - O sistema valida os dados submetidos. |
| | 4 - São persistidas as informações do usuário. |
| | 5 - Após a inserção, o sistema redireciona para a visão de login, com a mensagem de usuário cadastrado com sucesso. | 

## Fluxo Alternativo I - Dados inválidos
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 4.1 - O sistema apresenta novamente o formulário, com uma mensagem para o usuário corrigir os dados inválidos. |  
| (retorna ao passo 1 do fluxo principal) | |

## Fluxo Alternativo II - Senhas informadas são diferentes
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 4.2 - O siste apresenta novamente o formulário, com uma mensagem de senhas informadas diferentes. |  
| (retorna ao passo 1 do fluxo principal) | |

## Diagrama de Interação (Sequência ou Comunicação)

### Sequência parte 1
![Parte 1](./imgs/CDU%2011%20-%20sq%201.png)

### Sequência parte 2
![Parte 2](./imgs/CDU%2011%20-%20sq%202.png)

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...