# Agente de Busca com LangChain e Groq

Este projeto demonstra a criação de um agente de busca utilizando as bibliotecas `langchain`, `langchain_groq` e `langchain_community`. O agente é capaz de realizar buscas na internet e responder a perguntas com base nos resultados.

## Pré-requisitos

* Python 3.x
* Git

## Instalação

Siga os passos abaixo para configurar o projeto no seu ambiente local.

### 1. Clonar o Repositório

Primeiro, clone o repositório do GitHub para sua máquina local usando o seguinte comando:

```bash
git clone [https://github.com/lucansdev/agente_aula_AIDA.git](https://github.com/lucansdev/agente_aula_AIDA.git)
cd agente_aula_AIDA
```
### No windows
```bash
python -m venv venv
venv\Scripts\activate
``` 

### No macOS e no Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar Dependências

```bash
pip install langchain langchain_community langchain_groq python-dotenv google-search-results
```

###  Executar o Código
```bash
python seu_script_aqui.py
```

### Configurar as Chaves de API
Para que o agente funcione, você precisa de chaves de API para o Groq e para a Serper API.

Crie um arquivo chamado .env na raiz do projeto.

Groq API Key: Você pode obter a sua chave em https://console.groq.com/keys.

Serper API Key: Você pode obter a sua chave em https://serper.dev/.
