# 🤖 Chatbot com Gemini (IA da Google)

Este é um projeto de chatbot desenvolvido como trabalho acadêmico. O sistema utiliza a API do **Gemini**, inteligência artificial da Google, para responder às interações do usuário. O frontend foi desenvolvido com **React**, e o backend com **Python**.

---

## 🚀 Tecnologias Utilizadas

- ⚛️ **React** – Interface com o usuário (frontend)
- 🐍 **Python** – Backend e integração com a API Gemini
- 🌐 **Gemini API (Google AI)** – Geração de respostas com inteligência artificial
- 📦 **Axios** – Comunicação entre frontend e backend
- 🔧 **Flask (ou outro framework, dependendo do seu backend)**

---

## 📁 Estrutura do Projeto

```bash
chatboot/
│
├── backend/
│   ├── .env                    # Chave da API do Gemini
│   ├── server.py               # Servidor principal em Python
│   ├── ai_integration.py       # Lógica de comunicação com a API Gemini
│   └── __pycache__/            # Cache do Python
│
├── frontend/
│   ├── public/                 # Arquivos públicos
│   │   ├── imagemFundo.png
│   │   └── index.html
│   │
│   ├── src/                    # Código React
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── index.css
│   │   ├── Chatbot.jsx
│   │   └── Chatbot.css
│   │
│   ├── package.json
│   └── .env                    # (se necessário)
│
├── .gitignore
└── README.md

                                                ⚙️ Como Executar o Projeto

1. Clone o repositório

git clone https://github.com/leandrookamada/chatboot.git
cd chatboot


2. Configure o backend (Python)

Acesse a pasta:
cd backend
Instale as dependências:
pip install -r requirements.txt

Se não tiver o requirements.txt, crie com:
pip freeze > requirements.txt

Adicione sua chave da API do Gemini no arquivo .env:
GEMINI_API_KEY=sua-chave-aqui

Rode o backend:
python server.py


3. Configure o frontend (React)

Acesse a pasta:
cd ../frontend

Instale as dependências:
npm install

Rode o projeto:
npm start




🔑 Como obter a API Key do Gemini
Acesse https://aistudio.google.com/

Gere sua API Key

Coloque a chave no arquivo .env da pasta backend como mostrado acima

💡 Funcionalidades
Interface de chat amigável

Respostas geradas com IA (Gemini)

Comunicação entre frontend (React) e backend (Python)

Estrutura separada para facilitar manutenção

🧠 Objetivo Acadêmico
Este projeto foi desenvolvido para explorar:

Consumo de APIs com inteligência artificial

Integração entre frontend e backend

Desenvolvimento fullstack com React e Python

📫 Contato
Desenvolvido por Leandro Kamada – Projeto universitário.

yaml
Copiar
Editar
