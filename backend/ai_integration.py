import google.generativeai as genai
import os

class GeminiAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash-latest")
        self.chat_session = self.model.start_chat(history=[])

    def generate_response(self, chat_history):
        try:
            # Garante que o prompt contenha sempre a instrução de linguagem simples
            user_input = chat_history[-1]["parts"][0]["text"]
            if "linguagem simples" not in user_input.lower():
                user_input += (
                    "\n\nExplique com linguagem simples, como se estivesse falando com alguém leigo. "
                    "Evite jargões e use exemplos do dia a dia sempre que possível."
                )

            # Envia apenas a última mensagem com o contexto do chat session
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            print("Erro ao gerar resposta:", e)
            return "Desculpe, não consegui responder agora."

# Classe de fallback (não implementada ainda)
class OpenAI:
    def __init__(self, api_key):
        pass
    
    def generate_response(self, chat_history):
        return "Integração com OpenAI ainda não implementada."

def get_ai_provider(api_type, api_key):
    if api_type == "gemini":
        return GeminiAI(api_key)
    elif api_type == "openai":
        return OpenAI(api_key)
    else:
        raise ValueError("API desconhecida")
