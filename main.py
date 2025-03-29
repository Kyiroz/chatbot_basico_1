from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage #Los AIMessage responden a los HumanMessage
from schemas.schema import Bot

#Instancia de FastAPI
app = FastAPI()

#Para hacer el chatbot

# Cargar las variables del archivo .env
load_dotenv()

# Acceder a la clave secreta
COHERE_API_KEY = os.getenv('COHERE_API_KEY')

# Agregarla al entorno virtual
os.environ['COHERE_API_KEY'] = COHERE_API_KEY

#Instancia del modelo
#model = ChatCohere(cohere_api_key=COHERE_API_KEY, model="command-r")
model = ChatCohere(api_key=COHERE_API_KEY)


#DB
users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "test@mail.com",
        "age": 25
    },
    {
        "id": 2,
        "name": "Kyiro",
        "email": "mondongo@mail.com",
        "age": 20
    }
]

@app.get("/")
def hello_world():
    return {
        "Hello": "World"
        }

#get all users
@app.get(
        "/users",
        )
def get_all_users()->dict:
    return {
        "messages": "Succesfully fetched all users",
        "data": users
    }

class User(BaseModel):
    name: str
    email: str
    edad: int

@app.get(
        "/users/{user_id}"
        )

def get_user_by_id(user_id: int)->dict:
    for user in users:
        if user["id"] == user_id:
            return {
                "messages": "Succesfully fetched user",
                "data": user
            }
    raise HTTPException(status_code=404, detail="User not found")

@app.post(
        "/users",
          )
def create_user(user: User)->dict:
    user_data = user.model_dump()
    return {
        "messages": "Succesfully created user",
        "data": user_data
    }

#@app.post("/prompt",)
#def entrada(prompt: Bot)->dict:
#    user_prompt = prompt.model_dump()
#    return {
#        "messages": "Succesfully created user",
#        "data": user_prompt
#    }


'''
#Creamos la lista
historial = [
    #Despues de un SystemMessage siempre viene un HumanMessage
    SystemMessage(content="Eres una IA llamada Ultron que quiere conquistar el planeta Tierra"),
    HumanMessage(content="Hola, ¿como te llamas?"),
]

while True:
  try:
    input_message = "Hola" #Input del usuario

    #if input_message.lower() in ["q", "exit",]:
    #  print("Hasta luego!")
    #  break

    #Agregar al historial
    historial.append(HumanMessage(content=input_message))

    #Invoke model
    print("Pensando...")
    response = model.invoke(historial)

    if not response or not hasattr(response, "content"):
      print("Error: Respuesta invalida de la API")
      continue

    #Mostrar y guardar respuesta
    print(f"\nAgente: {response.content}\n" )
    historial.append(AIMessage(content=response.content))


    #print(response.content)

  except KeyboardInterrupt:
    print("\nInterrupcion por usuario. Saliendo...")
    break
  except Exception as e:
    print(f"Error critico: {str(e)}")
    break


@app.post("/chat")
def chat_with_ai(prompt: Bot):
    # Agregar el mensaje al historial
    input_message = prompt.prompt
    historial.append(HumanMessage(content=input_message))

    try:
        # Invocar el modelo
        response = model.invoke(historial)

        if not response or not hasattr(response, "content"):
            raise HTTPException(status_code=500, detail="Respuesta inválida del modelo")

        # Guardar la respuesta en el historial
        historial.append(AIMessage(content=response.content))

        # Retornar la respuesta al cliente
        return {
            "user_input": input_message,
            "ai_response": response.content,
            "historial": [msg.content for msg in historial],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error crítico: {str(e)}")
'''

class Persona(BaseModel):
    name: str
    email: str
    edad: int
    city: str
    direccion: str

@app.post(
        "/Register",
          )
def create_persona(user: Persona)->dict: #Si convierto la funcion a dict, tengo que retornar un dict, sino un objeto
    #return {
    #    "messages": "Succesfully created user",
    #    "data": f"User: {user.name}"
    #}
    return "Hola mundo"



#class Bot(BaseModel):
#    pregunta: str

#Creamos la lista
historial = [
    #Despues de un SystemMessage siempre viene un HumanMessage
    SystemMessage(content="Eres una IA llamada Ultron que quiere conquistar el planeta Tierra"),
    HumanMessage(content="Hola, ¿como estas?"),
]

#while True:
#  try:
#    input_message = "Hola" #Input del usuario

    #if input_message.lower() in ["q", "exit",]:
    #  print("Hasta luego!")
    #  break

    
  
@app.post("/chat")
def chat_bot(chat: Bot):
   
    input_message = chat.pregunta #Input del usuario
    #Agregar al historial
    historial.append(HumanMessage(content=input_message))
    
    #while True: #Si dejo el while, se guardaran las conversaciones, sino no
    #  try: 
    #Invoke model
    print ("Pensando...")
    response = model.invoke(historial)
    if not response or not hasattr(response, "content"):
      print("Error: Respuesta invalida de la API")
      #continue
    #Mostrar y guardar respuesta
    print (f"\nAgente: {response.content}\n" )
    historial.append(AIMessage(content=response.content))
    
    return {
        "HumanMessage": input_message,
        "AImessage": response.content,
        "Historial": historial[-2].content #o tambien  
    }
            
      #except KeyboardInterrupt:
      #  print("\nInterrupcion por usuario. Saliendo...")
      #  break
      #except Exception as e:
      #  print(f"Error critico: {str(e)}")
      #  break