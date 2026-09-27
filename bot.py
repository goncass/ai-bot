import requests


def perguntar(prompt):
    try:
        resposta = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3.2", "prompt": prompt, "stream": False},
        )
        return resposta.json()["response"]
    except Exception as e:
        return f"Erro: {e}"


print("Bot de IA — escreve 'sair' para terminar")

while True:
    pergunta = input("Tu: ")
    if pergunta.lower() == "sair":
        break
    print("Bot:", perguntar(pergunta))

print("Até à próxima!")
