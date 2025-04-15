from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from flask_cors import CORS
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a chave da API do Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Criar a aplicação Flask
app = Flask(__name__)
CORS(app)

# Prompt inicial focado no contexto brasileiro
inicial_prompt = {
    "role": "user",
    "parts": [{
        "text": (
            "Você é um assistente jurídico especializado em Direitos Humanos no Brasil. "
            "Sempre que te perguntarem sobre direitos, dê prioridade às leis brasileiras, "
            "como a Constituição Federal de 1988, o Estatuto da Criança e do Adolescente (ECA), "
            "a CLT e o Código Civil. Responda de forma clara e acessível, como se estivesse explicando para uma pessoa leiga."
        )
    }]
}

# Inicializar histórico da conversa
chat_history = [inicial_prompt]

# Endpoint principal de chat
@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    data = request.get_json()
    user_message = data.get("message", "")

    # Adiciona a mensagem do usuário ao histórico
    chat_history.append({"role": "user", "parts": [{"text": user_message}]})

    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(chat_history)
        bot_reply = response.text

        # Adiciona a resposta da IA ao histórico
        chat_history.append({"role": "model", "parts": [{"text": bot_reply}]})

    except Exception as e:
        print("Erro:", e)
        bot_reply = "Desculpe, não consegui responder agora."

    return jsonify({"reply": bot_reply})

# Endpoint para resetar a conversa
@app.route("/reset", methods=["POST"])
def reset():
    global chat_history
    chat_history = [inicial_prompt]
    return jsonify({"message": "Histórico resetado com contexto brasileiro!"})

# Rodar o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
