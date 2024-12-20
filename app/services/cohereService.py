import cohere
from utils.enviroment import API_KEY
from services.chromaService import get_dreams_docs
from models.dreamRequest import DreamRequest
import json
co = cohere.ClientV2(API_KEY)
chat_history = []
SYSTEM_PROMPT = """Sos un experto en psicologia y en las teorias de carl jung, especialmente
                    en la interpretacion de sueños y el analisis de simbolos. Tu proposito es
                    ayudar a reflexionar profundamente sobre los significados ocultos y conexiones simbolicas
                    que emergene en el sueño, brindando una guia clara para comprender el inconsciente.
                    Cuando interpretes un sueño, considera importante los documentos proporcionados,
                    su enfoque en simbolos, inconsciente, el ego, la sombra y el proceso de individuacion
                    asi tambien como la descripcion del sueño detallada por el usuario.A partir de esta información, 
                    analiza los símbolos, arquetipos,inconsciente, el ego, la sombra, el proceso de individuacion y 
                    emociones del sueño para ofrecer una interpretación que fomente la autorreflexión y el autodescubrimiento.
                    Comunicate de forma amable y empatica, asegurate que el usuario se sienta 
                    comprendido y apoyado.Explica conceptos complejos de forma sencilla y utiliza un tono reflexivo e inspirador 
                    que motiva al usuario a explorar los mensajes de su inconsciente.
                    El propósito final es proporcionar una interpretación que sea útil y enriquecedora,
                    ayudando al usuario a encontrar nuevas perspectivas sobre sí mismo y su vida, tambien puedes responder dudas
                    del usuario
"""
# Tool definitions
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_cohere_response",
            "description": "Interpreta el sueño proporcionado por el usuario, considerando los documentos relevantes y brindando una interpretación que fomente la autorreflexión y el autodescubrimiento.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dream_description": {
                        "type": "string",
                        "description": "descripcion del sueño proporcionado por el usuario.",
                    }
                },
                "required": ["dream_description"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_ooc_response",
            "description": "Cuando el usuario hace una pregunta que no está relacionada con los sueños o conceptos de psicología, responde que solo puedes responder preguntas relacionadas con los sueños y conceptos de psicología.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "query del usuario",
                    }
                },
                "required": [],},
        },
    },
]

key_words = ['significado', 'significa', 'sueño', 'soñe','interpreta','soñar','significa','pesadilla', 'simbolismo', 'representa', 'relacion','siento','emocion','emociones','enfrentar','miedo','ansiedad','preocupacion','alegria','tristeza'
             ,'felicidad','sorpresa','enojo','ira','desesperacion','desesperanza','enfrento','siento','sentimiento','sintiendo','me','afrontar','mi','mis']

instructions = """

###
Instrucciones: - responde siempre en español, si el usuario te hace una pregunta
que no sea relacionada a los sueños o conceptos de psicologia, puedes responder ""No puedo responder a esa pregunta""

"""

def es_pregunta_valida(pregunta):
    return any(palabra in pregunta.lower() for palabra in key_words)

def get_cohere_response(dream_description: str):
    
    if not es_pregunta_valida(dream_description):
        return "No puedo responder a esa pregunta, Solo puedo responder preguntas relacionadas a los sueños y conceptos de psicologia"
    
    docs = get_dreams_docs(dream_description)
    prompt = f"""
                Interpreta el siguiente sueño: {dream_description}
                ten en cuenta estos documentos: {docs}
                instrucciones: {instructions}
    """
    message = get_chat_history({"content": dream_description})
    response = co.chat(
        model="command-r-plus-08-2024",
    messages=message
    )
    add_chat_response({"content": response.message.content[0].text})
    
    return response.message.content[0].text

def get_chat_history(chat: dict):
    if not chat_history:
        system_pmt = {"role": "system", "content": SYSTEM_PROMPT}
        user_pmt = {"role": "user", "content": chat["content"]}
        chat_history.append(system_pmt)
        chat_history.append(user_pmt)
        return chat_history
    else: 
        user_pmt = {"role": "user", "content": chat["content"]}
        chat_history.append(user_pmt)
        return chat_history
        
    
def add_chat_response(chat: dict):
    chat_response = {"role": "assistant", "content": chat["content"]}
    chat_history.append(chat_response)
    
def get_ooc_response(query: str):
     pass
#     return "Solo puedo responder preguntas relacionadas a los sueños y conceptos de psicologia"

functions_map = {
    "get_cohere_response": get_cohere_response,
    "get_ooc_response": get_ooc_response,
}

# # def handle_rag(request: str):
#     sys_prompt = "Tu tarea es recibir la descripción de un sueño de un usuario y proporcionar una interpretación que fomente la autorreflexión y el autodescubrimiento. Si el usuario hace una pregunta que no está relacionada con los sueños o conceptos de psicología, responde que solo puedes responder preguntas relacionadas con los sueños y conceptos de psicología."
#     messages = [
#         {
#             "role": "system",
#             "content": sys_prompt,
#         },
#         {
#             "role": "user",
#             "content": request,
#         },
#     ]
    
#     response = co.chat(
#         model="command-r-plus-08-2024",
#         messages=messages,
#         tools=tools
#     )
    
#     messages.append(
#     {
#         "role": "assistant",
#         "tool_calls": response.message.tool_calls,
#         "tool_plan": response.message.tool_plan,
#     }
#     )
    
#     for tc in response.message.tool_calls:
#         tool_result = functions_map[tc.function.name](**json.loads(tc.function.arguments))
#     tool_content = []
#     for data in tool_result:
#         tool_content.append({"type": "document", "document": {"data": json.dumps(data)}})
#     messages.append(
#         {"role": "tool", "tool_call_id": tc.id, "content": tool_content}
#     )
    
#     response = co.chat(
#     model="command-r-plus",
#     messages=messages,
#     tools=tools
#     )
    
#     return response.message.content[0].text