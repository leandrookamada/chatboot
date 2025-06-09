import { useState, useEffect, useRef } from "react";
import "./Chatbot.css";

function Chatbot() {
  const [messages, setMessages] = useState([
    {
      text: "Olá, sou o seu assistente virtual para tirar sua dúvidas sobre o sistema legislativo brasileiro. Eai? por onde começamos? 😉",
      sender: "bot",
    },
  ]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const formatReply = text => {
    let formattedText = text.replace(/\*\*/g, ""); // Remove os **
    formattedText = formattedText.replace(/\* (.+)/g, "<li>$1</li>"); // Converte listas
    return formattedText.replace(/(<li>.+<\/li>)/g, "<ul>$1</ul>"); // Garante que listas fiquem dentro de <ul>
  };

  const handleSend = async () => {
    if (input.trim() === "") return;

    const newMessages = [...messages, { text: input, sender: "user" }];
    setMessages(newMessages);
    setInput("");
    setIsTyping(true);

    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();
      const formattedReply = formatReply(data.reply);
      setMessages([...newMessages, { text: formattedReply, sender: "bot" }]);
    } catch (error) {
      console.error("Erro ao enviar mensagem:", error);
      setMessages([
        ...newMessages,
        { text: "Erro ao conectar com o servidor.", sender: "bot" },
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  const handleKeyPress = e => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.sender}`}
            dangerouslySetInnerHTML={{ __html: msg.text }}
          />
        ))}
        {isTyping && <div className="typing">Bot está digitando...</div>}
        <div ref={messagesEndRef} />
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Digite sua dúvida..."
        />
        <button onClick={handleSend}>Enviar</button>
      </div>
    </div>
  );
}

export default Chatbot;
