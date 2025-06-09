from flask import Flask, request, jsonify
import os
from flask_cors import CORS
from dotenv import load_dotenv
from ai_integration import get_ai_provider  # Função para escolher o provedor de IA

# Carregar variáveis de ambiente
load_dotenv()

# Obter chave da API do .env
api_key = os.getenv("GOOGLE_API_KEY")

# Criar a aplicação Flask
app = Flask(__name__)
CORS(app)

# Prompt inicial com foco em linguagem simples e inclusiva
inicial_prompt = {
    "role": "user",
    "parts": [{
        "text": (
            "Você é um assistente jurídico especializado em Direitos Humanos no Brasil. "
            "Sempre que responder, utilize leis brasileiras como a Constituição Federal de 1988, o ECA, a CLT e o Código Civil. "
            "Explique tudo com linguagem **simples, acessível e sem jargões jurídicos**, como se estivesse explicando para uma pessoa comum. "
            "Use exemplos do cotidiano sempre que possível e evite copiar a lei sem explicar o que ela significa."
        )
    }]
}

# Histórico da conversa
chat_history = [inicial_prompt]

# Inicializar o provedor de IA (Gemini por padrão)
ai_provider = get_ai_provider("gemini", api_key)

# Endpoint principal de chat
@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    data = request.get_json()
    user_message = data.get("message", "")

    # Reforçar a linguagem simples em cada mensagem
    user_prompt = (
        f"{user_message}\n\n"
        "Explique com linguagem simples, como se estivesse falando com alguém que não entende de leis. "
        "Use exemplos do dia a dia se possível."
    )

    # Adiciona ao histórico
    chat_history.append({"role": "user", "parts": [{"text": user_prompt}]})

    # Obter resposta da IA
    bot_reply = ai_provider.generate_response(chat_history)

    # Adiciona resposta ao histórico
    chat_history.append({"role": "model", "parts": [{"text": bot_reply}]})

    return jsonify({"reply": bot_reply})

# Endpoint para resetar o histórico
@app.route("/reset", methods=["POST"])
def reset():
    global chat_history
    chat_history = [inicial_prompt]
    return jsonify({"message": "Histórico resetado com contexto jurídico brasileiro e linguagem simples."})

# Rodar o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
