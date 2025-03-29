import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere

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