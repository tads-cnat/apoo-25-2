# CDU 17. Moderar publicação de portifólio 

- **Ator principal**: Administrador.
- **Atores secundários**: não possui.	 
- **Resumo**: o administrador realiza uma ação de moderação quanto a um portifólio de um dado aluno. As ações possíveis são: (i) suspender a publicação de um projeto específico OU (ii) suspender a publicação do portifólio como um todo, adicionando uma justificativa para tal.
- **Pré-condição**: portifólio devidamente cadastrado com vários projetos.
- **Pós-Condição**: projeto/portifólio terá a sua visualização suspensa para o público.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| 0 - visualizando a lista de alunos com portifólio publicado, o administrador seleciona a opção moderar portifólio associado a um dado aluno | |  
| | 1 - o sistema apresenta algumas informações do aluno e a lista dos projetos. Ao lado das informações gerais e ao lado de cada projeto o sistema apresenta uma caixa de seleção (para suspender publicação). Ao final, é apresentado uma caixa de texto para uma justificativa e um botão para submeter |
| 2 - o administrador seleciona o portifólio como um todo OU um ou mais projetos específicos para suspender a publicação, informa uma justificativa e submete o formulário | |
| | 3 - o sistema apresenta novamente as informações do portifólio, contendo agora uma marcação especial indicando a suspensão da publicação do portifólio como um todo, OU assiciado aos projetos afetados |
| | 4 - nessa mesma tela, para cada indicação de suspensão deverá ser apresentado também um botão de ação para a reversão da suspensão |


## Fluxo Alternativo I - Nenhuma caixa de selação marcada
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: | 
| | 3.1 - retorna ao passo 2 do fluxo principal, contendo uma mensagem de erro indicando que ao menos uma seleção precisa ser feita - ou do portifólio como um todo ou de um (ou mais) projeto(s) específico(s) |  

## Fluxo Alternativo II - Seleção simultânea do portifólio e de projetos específicos
| Ações do ator | Ações do sistema |
| :-----------: | :--------------: |  
| | 3.2 - o sistema apresenta novamente as informações do portifólio, contendo agora uma marcação especial indicando a suspensão do portifólio como um todo (nesse caso, serão DESCONSIDERADAS as marcações individuais nos projetos) |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...