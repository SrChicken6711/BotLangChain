from typing import Any
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.tools import tool
from pathlib import Path

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    # temperature=0.3,
    max_output_tokens=500
)

tools_client : list[Any] = []
tools_admin : list[Any] = []

llm_client = llm.bind_tools(tools_client)
llm_admin = llm.bind_tools(tools_admin)

def load_prompt(ruta : str) -> str:
    return Path(ruta).read_text(encoding="UTF-8")

PROMPTS = {
    "client" : load_prompt("prompts\\client.md"),
    "admin" : load_prompt("prompts\\admin.md")
}

def respond(user_message : str, rol : str = "client") -> str:
    system_prompt = PROMPTS.get(rol, PROMPTS["client"])
    message = [
        SystemMessage(content=system_prompt),
        HumanMessage(content= user_message)
    ]
    try:
        if rol == "admin":
            answer = llm_admin.invoke(message)
        else:
            answer = llm_client.invoke(message)
        
        content = answer.content
    
        if isinstance(content, list):
            textos: list[Any] = [
                bloque.get("text", "")
                for bloque in content
                if isinstance(bloque, dict) and bloque.get("type") == "text"
            ]
            return "".join(textos)
    
        return str(content)
    except Exception as e:
        return f"Error al tratar de generar respuesta: {e}."

