import requests
import json
import os

OLLAMA_API_URL = "http://ollama.eastus.cloudapp.azure.com:11434/api/generate"
MODEL_NAME = "phi3:mini"

def get_user_prompt():
    """Solicita a mensagem (prompt) ao usuário."""
    print("--- Cliente Ollama (Modelo: phi3:mini) ---")
    print("Digite sua mensagem. Digite 'sair' para encerrar.")
    
    while True:
        prompt = input("Você: ")
        if prompt.lower() == 'sair':
            return None
        if prompt.strip():
            return prompt
        print("A mensagem não pode estar vazia.")

def send_prompt_to_ollama(prompt):
    """Envia o prompt para a API do Ollama e exibe a resposta."""
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": True
    }

    print("\nAI:")
    
    try:
        with requests.post(OLLAMA_API_URL, json=payload, stream=True) as response:
            
            if response.status_code != 200:
                print(f"\n[ERRO] Falha na API. Status Code: {response.status_code}")
                print(f"Resposta do servidor: {response.text}")
                return

            for chunk in response.iter_lines(decode_unicode=True):
                if chunk:
                    try:
                        data = json.loads(chunk)
                        
                        content = data.get("response", "")
                        
                        print(content, end="", flush=True)

                        if data.get("done"):
                            break
                            
                    except json.JSONDecodeError:
                        continue
            

            print("\n")

    except requests.exceptions.ConnectionError:
        print(f"\n[ERRO] Não foi possível conectar ao servidor Ollama em {OLLAMA_API_URL}. Verifique a URL ou a conexão.")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro inesperado: {e}")


def main():
    while True:
        prompt = get_user_prompt()
        
        if prompt is None:
            print("Encerrando a aplicação. Até logo!")
            break
        
        send_prompt_to_ollama(prompt)

if __name__ == "__main__":
    main()