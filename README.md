# Cliente Ollama Simples (phi3:mini)

Este projeto é um cliente de linha de comando (CLI) simples, escrito em **Python**, que se conecta a uma instância pública da API do **Ollama** para interagir com o modelo de linguagem **phi3:mini**.

O objetivo é demonstrar a comunicação pura via HTTP (requisições API) com um LLM, enviando um prompt do usuário e exibindo a resposta em tempo real (streaming).

## Como Funciona

A aplicação utiliza a biblioteca `requests` do Python para:
1.  Receber a entrada de texto (prompt) do usuário no terminal.
2.  Enviar a requisição `POST` para o endpoint `/api/generate` do servidor Ollama.
3.  Processar e exibir os dados (chunks de texto) conforme são recebidos da API (modo **streaming**).

## Requisitos

Para rodar esta aplicação, você precisa ter o seguinte instalado:

* **Python 3.x** (Recomendado 3.8 ou superior)
* **pip** (gerenciador de pacotes do Python)

## Configuração e Execução

Siga os passos abaixo para configurar e iniciar a aplicação.

### 1. Clonar o Repositório

Primeiro, clone este repositório para o seu ambiente local:

> git clone https://github.com/Gabrieelgc2/cliente-Ollama-em-Python-via-API-HTTP-.git

> cd Ollama


### 2. Instalar as Dependências
Instale a única dependência necessária (requests) listada no requirements.txt:
> pip install -r requirements.txt

### 3. Executar o Script
> python main.py


