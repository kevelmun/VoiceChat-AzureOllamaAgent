# from openai import OpenAI

# client = OpenAI(

#     base_url = 'http://localhost:11434/v1'
#     api_key='ollama3.2' 
# )

import ollama

mmodel = "loly"
conversation_history = []

def model_response(user_input):
    # Añadir el mensaje del usuario al historial
    conversation_history.append({'role': 'user', 'content': user_input})
    
    # Llamar al modelo con el historial actualizado
    response = ollama.chat(
        model=mmodel,
        messages=conversation_history
    )
    
    # Extraer el contenido de la respuesta
    response_content = response['message']['content']
    
    # Añadir la respuesta del asistente al historial
    conversation_history.append({'role': 'assistant', 'content': response_content})
    
    return response_content

# if __name__ == "__main__":
#     user_input = ""
#     while user_input.lower() != "exit":
#         user_input = input("Ingresa tu pregunta: ")
#         if user_input.lower() == "exit":
#             break
#         # Añadir el mensaje del usuario al historial
#         conversation_history.append({'role': 'user', 'content': user_input})
#         # Obtener la respuesta del modelo
#         response = model_response(conversation_history)
#         # Añadir la respuesta del asistente al historial
#         conversation_history.append({'role': 'assistant', 'content': response})
#         # Imprimir la respuesta
#         print(response)
