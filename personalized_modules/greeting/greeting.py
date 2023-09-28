# greeting.py
# Function to greeting
def greeting(nombre, lang):
  message = getLanguage(lang)
  if message:
    return f"{message}, {nombre}!"
  return errorMessage

def getLanguage(lang):
  if lang in messageGreeting.keys():
    return messageGreeting[lang]
  return False

# Variable with a message
errorMessage = "No se encontro el idioma indicado"
welcomeMessage = "¡Bienvenido a mi módulo personalizado!"
# Variable in different languages
messageGreeting = {
  'es':'Hola',
  'en':'Hi',
  'it':'Ciao',
  'fr':'Salut'
  }