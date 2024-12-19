import cohere
from utils.enviroment import API_KEY
from services.chromaService import get_dreams_docs


co = cohere.ClientV2(API_KEY)
chat_history = []
SYSTEM_PROMPT = """Sos unexperto en psicologia y en las teorias de carl jung, especialmente
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


# output_format = """
# # interpretacion
# *Interpretacion general*: (texto)
# - simbolo: descripcion
# -  simbolo 2: descripcion
# ## reflexion final
# (texto)

# -pregunta que invita a la reflexion
# """

def get_cohere_response(description: str):
    
    docs = get_dreams_docs(description)
    prompt = f"""
                Interpreta el siguiente sueño: {description}
                ten en cuenta estos documentos: {docs}
    """
    message = get_chat_history({"content": description})
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
    
