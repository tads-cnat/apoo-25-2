# CDU01. Gerenciar portifólio 

- **Ator principal**: Aluno TADS.
- **Atores secundários**: não existe. 
- **Resumo**: o aluno de TADS preenche um fomulário de cadastramento de novo PROJETO. Dado que o portifólio do aluno é composto dos vários projetos que este aluno participou.
- **Pré-condição**: Aluno devidamente cadastrado e autenticado.
- **Pós-Condição**: Novo projeto é adicionado ao portifólio do aluno em questão.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - o aluno clica no botão "novo projeto" | |  
| | 1 - o sistema exibe um formulário de cadastramento de projeto (nome*, imagem, descrição*, semestre letivo de início*, duração, link para o repositório, tecnologias*, fase, estado*, integrantes, orientador) - *obrigatórias |
| 2 - o aluno preenche as informações solicitadas e submete o formulário | |
| | 3 - o sistema valida as informações |
| | 4 - o sistema persiste as informações e retorna a lista dos projetos do aluno, exibindo uma mensagem de "cadastro realizado com sucesso" | 

## Fluxo Alternativo I - Informações inválidas
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 4.1 - o sistema torna a exibir o fomulário, destacando as informações que faltaram (obrigatórias) ou estavam inválidas, e pede que o aluno as corrija. |  
| (retorna ao passo 2 do fluxo principal) | |

## Fluxo Alternativo II - Listagem dos projetos de aluno
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0.2 - o aluno seleciona a opção de "visualizar portfólio" | |  
| | 1.2 - o sistema lista todos os projetos que fazem parte do portfólio do aluno |
| | 2.2 - os projetos são listados em uma tabela com as seguintes colunas: título, descrição (50 caracteres), ano de início e estado (ordenados por ano de início) |
| (fluxo finalizado) ||  

## Fluxo Alternativo III - Alteração de dados de um projeto
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0.3 - na tela de listagem dos projetos, é selecionada a opção de alterar um do projeto | |  
| | 1.3 - o sistema exibe um formulário equivalente ao de cadastro, só que preenchido |
| 2.3 - o aluno altera as informações que desejar e submete o formulário | |
| | 3.3 - o sistema valida as informações que forem preenchidas |
| | 4.3 - o sistema indica os campos inválidos OU apresenta mensagem de sucesso |
| (fluxo finalizado) | |

## Fluxo Alternativo IV - Remoção de um dado projeto
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0.4 - na tela de listagem dos projetos, é selecionada a opção de alterar um do projeto | |  
| | 1.4 - o sistema solicita uma confirmação do aluno |
| 2.4 - o aluno confirma a solicitação de remoção | |
| | 3.4 - o sistema relaiza a remoção e apresenta uma mensagem de sucesso |
| (fluxo finalizado) | |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...