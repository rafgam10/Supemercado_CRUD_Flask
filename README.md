# SuperCompras - Sistema de Gestão de Estoque

SuperCompras é um sistema de gerenciamento de estoque básico, desenvolvido para facilitar as operações de cadastro, visualização, edição e remoção de produtos. Este projeto utiliza o framework Flask e armazena os dados temporariamente na memória, permitindo que o sistema funcione enquanto o servidor está em execução, sem persistência de dados.

## Funcionalidades

O sistema oferece as seguintes operações CRUD:
- **Create (Criar)**: Permite adicionar novos produtos com nome, categoria, preço e quantidade.
- **Read (Ler)**: Lista todos os produtos cadastrados.
- **Update (Atualizar)**: Permite editar informações de produtos específicos.
- **Delete (Excluir)**: Remove produtos da lista temporária.

## Pré-requisitos

- Python 3.x
- Flask (instalado via pip)

## Instalação

1. **Clone o repositório** para seu ambiente local.
   ```bash
   git clone https://github.com/seu-usuario/supercompras.git
   cd supercompras

2. **Instale as dependências**. No terminal, execute:

    ```bash
    pip install flask

3. **Executando o Projeto**:

- **Inicie o servidor Flask executando o seguinte comando na pasta do projeto:**
    ```bash
    python app.py

- **Acesse o sistema no navegador: Abra seu navegador e vá para:** http://127.0.0.1:5000


