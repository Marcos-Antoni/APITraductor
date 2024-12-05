from googletrans import Translator

# Crear una instancia del traductor
traductor = Translator()
 
texto = "hi"

# Texto a traducir

# Traducir al inglés
traduccion = traductor.translate(texto)

# Mostrar la traducción
print(traduccion.text)  
  