# 🚀 Trilha de FastAPI - Eduardo Mendes


### 🛠️ Configurações do  Ambiente de Desenvolvimento para o projeto:

A configuração do ambiente é feita utilizando o **Poetry** para o gerenciamento de dependências. Para auxiliar na formatação e padronização do código, são utilizados **linters** como o **Ruff** e **Taskipy** para a execução automatizada de tarefas.

### 📦 Dependências

- **Poetry**: Gerenciamento de dependências
- **Taskipy**: Automação de tarefas
- **Ruff**: Linter para garantir a qualidade e consistência do código

## 🧪 Testes e Desenvolvimento

O desenvolvimento da aplicação seguiu a metodologia **TDD** (Desenvolvimento Orientado a Testes) e a cobertura de testes foi garantida com as seguintes bibliotecas:

- **Pytest**: Testes unitários
- **pytest-cov**: Cobertura de testes
- **Factory Boy**: Criação de objetos de teste
- **Freezegun**: Mock de datas
- **Testcontainers**: Criação de containers para testes de integração


## 🏗️ Modelagem e Banco de Dados

A modelagem de dados foi realizada utilizando **Pydantic** e **SQLAlchemy** para garantir a validação e o gerenciamento eficaz dos dados. A migração do banco de dados foi feita com **Alembic** e o banco de dados utilizado é o **PostgreSQL**.

### 🛠️ Tecnologias Utilizadas:

- **Pydantic**: Validação de dados
- **SQLAlchemy**: ORM para interação com o banco de dados
- **Alembic**: Ferramenta para migração de dados
- **PostgreSQL**: Banco de dados relacional

## 🔐 Autenticação e Autorização com JWT

A aplicação implementa autenticação utilizando **OAuth2** com tokens **JWT**, garantindo uma abordagem segura para a autenticação de usuários.

- Implementando autenticação com JWT
- Protegendo rotas com dependências
- Gerenciando permissões e acessos


## 🐳 Docker

A aplicação foi dockerizada com Docker, e utiliza  docker compose para orquestrar os containers da Aplicação e PostgreSQL


## 🌐 Deploy da APlicação 

A aplicação está sendo servida no Fly.io e você poderá testar os endpoints no link abaixo. 

https://fast-course.fly.dev/docs


## 📚 Recursos Adicionais

- [Link do Curso Completo](https://fastapidozero.dunossauro.com/aulas/sincronas/)
- [Documentação do FastAPI](https://fastapi.tiangolo.com/)
- [Documentação do Pydantic](https://pydantic-docs.helpmanual.io/)
- [Documentação do SQLAlchemy](https://www.sqlalchemy.org/)
- [Documentação do pytest](https://docs.pytest.org/)
- [Documentação do Docker](https://docs.docker.com/)

