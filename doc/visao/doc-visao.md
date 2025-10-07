# Documento de Visão

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| :--: | :----: | :-------: | :-----: |
| 02/10/25 | 1.0 | Versão inicial | Fellipe Aleixo |
| 07/10/25 | 1.1 | Complementando e fechando a primeira versão | Fellipe Aleixo |
| - | - | - | - |


## 1. Visão Geral do Sistema Proposto

O objetivo central do sistema é possibilitar aos alunos do curso superior de Tecnologia em Análise e Desenvolvimento de Sistemas (TADS) do campus Natal Central (CNAT) do IFRN terem acesso facilitado a oportunidades de prática profissional (p.ex.: estágios). Para tal, o sistema atuará em duas frentes: no ponto de vista dos alunos, possibilitará a publicação dos portfólios individuais de projetos, bem como um relato das experiências adiquiridas. Já do ponto de vista das empresas/instituições, o sistema possibilitará a divulgação das suas oportunidades de vagas, recebendo como retorno uma lista dos alunos que se interessaram pela vaga.

## 2. Descrição do Problema
| | |
| :-: | :-: |
| **Problema** | Dificuldade dos alunos de TADS em terem fácil acesso à oportunidades de prática profissional |
| **Afeta** | Alunos de TADS |  
| **Impacta** | A prática profissional é um componente fundamental da formação de TADS |
| **Solução** | Um sistema que facilite o acesso dos alunos de TADS à oportunidades de prática profissional | 

## 3. Descrição dos Usuários 

| Usuário | Descrição | Responsabilidades |
| :-----: | :-------: | :--------------: |
| Administrador | usuário que atuará na função de administrador do sistema | atuar como moderador de conteúdos, habilitar usuários externos, etc. |
| Aluno de TADS | alunos cursando TADS, preferêncialmente a partir do 3º período | publicar as informações do seu portfólio e sinalizar o interesse em oportunidades de vaga |
| Recrutador | usuários externos, representando empresas ou instituições | publicação de vagas de estágio e/ou contratação, tendo acesso a uma lista dos interessados nas vagas |

## 4. Descrição do Ambiente dos Usuários

| Usuário | Ambiente operacional |
| :-----: | :------------------: |
| Administrador | utilizará um computador pessoal com acesso à Internet |
| Aluno de TADS | utilizará um computador OU aparelho celular com acesso à Internet |
| Recrutador | utilizará um computador pessoal com acesso à Internet |

## 5. Principais Necessidades dos Usuários

1. **Administrador**
   - Analisar e habilitar usuários representando empresas/instituições;
   - Garantir que nenhum conteúdo inadequado seja postado no sistema; 
1. **Aluno de TADS**
   - Divulgar o seu portifólio de projetos de desenvolvimento de sistemas;
   - Descrever as experiências obtidas através dos projetos;
   - Buscar por vagas específicas;
   - Ser avisado quando do cadastramento de vagas específicas;
   - Sinalizar o intgeresse em vagas específicas;
1. **Recrutador**
   - Publicizar as oportunidades de vaga na empresa/instituição;
   - Pesquisar por alunos com perfis de interesse;
   - Receber as informações dos alunos que sinalizaram interesse em vagas ofertadas.


## 6. Alternativas Concorrentes

1. **Linkedin**
   - Rede Social Profissional e de Negócios;
   - O perfil do usuário atua como um currículo virtual completo e interativo. Ele vai além do texto estático, permitindo a adição de: portfólio multimídia; recomendações e endossos de habilidades; artigos e publicações;
   - Ferramenta de Recrutamento e Busca por Oportunidades;
   - O LinkedIn evoluiu para ser um hub de conteúdo e desenvolvimento profissional;
1. **Indeed**
   - O Indeed é primariamente um agregador de vagas de emprego, mas evoluiu para incluir recursos como upload de currículo e busca por candidatos;
   - Maior plataforma de recrutamento do mundo em termos de tráfego e volume de vagas;
   - Para muitas empresas e candidatos, a jornada de busca por emprego começa no Indeed, e não no LinkedIn, tornando-o um concorrente formidável na função principal de conectar candidatos a vagas;
1. **Glassdoor**
   - O Glassdoor é mais conhecido pelas avaliações anônimas de empresas, salários e entrevistas;
   - Ao agregar vagas de emprego e permitir que os usuários pesquisem informações sobre culturas empresariais, ele tornou-se uma ferramenta essencial na jornada do candidato;
   - Muitos profissionais usam o LinkedIn para se conectar e o Glassdoor para pesquisar a empresa antes de uma entrevista.

## 7. Regras de Negócio

| ID  | Regra | Descrição |
| :-: | :---: | :-------: |
| RN01 | Exclusividade para TADS | Para publicar o seu portfólio, é necessário comprovar ser aluno de TADS/CNAT/IFRN |
| RN02 | Limite de 10 projetos | Na versão inicial o sistema limitará o número de projetos por aluno |
| RN03 | Vários participantes de um projeto | Vários alunos podem estar associados a um mesmo projeto, mas cada um relata as experiência (individuais) que foram adiquiridas |

## 8. Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
| :----: | :--: | :-------: | :--------: |
| RF01 | Autenticação de usuários | Permitir o cadastramento e autenticação de usuárious alunos e recrutadores | média |
| RF02 | Publicação de vagas | Gerenciar o cadastro das informações das oportunidades de vaga | alta |
| RF03 | Publicação de portfólio | Gerenciar o cadastro do portfólio de projetos do aluno | alta |
| RF04 | Ajuste de perfil de usuário | Realização de ajustes nas informações do perfil do usuário | baixa |
| RF05 | Possibilitar aluno conconrrer à vaga | O aluno poderá sinalizar o interesse em uma vaga específiica que foi publicada | alta |
| RF06 | Comunicação entre usuários por meio de chat | Possibiliar usuários trocarem mensagens atravé do chat | média |
| RF07 | Comentários sobre vagas e portfólio | Possibilitar que as publicações de vaga e portfólio possam receber com | baixa |
| RF08 | Notificação de eventos aos usuários | Notificar usuários específicos que possa ser notificados e ocorrências no sistema | média |

> **Prioridade**: alta, média ou baixa

## 9. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| :----: | :--: | :-------: | :-------: | :-----------: |
| NF01 | Aplicação Web | O sistema deverá ser implementado na forma de uma aplicação Web | implementação | obrigatório |
| NF02 | Framework Python/Django | Deverá ser utilizado o framework Python/Django para a implementação | implementação | obrigatório |
| NF03 | Aplicação com Responsividade | A aplicação deverá ser apresentada de forma responsiva em dispositivos móveis | usabilidade | obrigatório |
| NF04 | De fácil manutenção | O sistema será mantido pelos próprios alunos de TADS, por isso precisará ser de fácil manutenção | suportabilidade | desejável | 

> **Categoria**: usabilidade, confiabilidade, performance, suportabilidade, restrição de projeto, implementação, interface e requisito físico - segundo classificação [FURP+](https://pt.wikipedia.org/wiki/FURPS).

> **Classificação**: desejável ou obrigatório.