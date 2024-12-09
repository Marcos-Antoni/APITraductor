from googletrans import Translator, LANGUAGES
import json


def listar_idiomas():
    array = {}
    for codigo, nombre in LANGUAGES.items():
        array[codigo] = nombre
    
    # Convertir el diccionario a JSON
    json_data = json.dumps(array, ensure_ascii=False)
    return json_data
    

class ClassTranslator:
    
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.traductor = Translator()    
        pass
    
    def FindSrc(self, text):
        if(self.src == ""):
            self.src = self.traductor.detect(text).lang
        pass            
    
    def FindDest(self):
        if self.dest != "":
            return
        
        if self.src == "es":
            self.dest = "en"
        else:
            self.dest = "es"
        
        pass
    
    def traducir(self,text):
        if(text == ""):
            return {"error":"No se ha enviado un texto"}
        
        self.FindSrc(text)
        self.FindDest()
          
        traducir = self.traductor.translate(text, src=self.src, dest=self.dest)
        
        data = {"text":traducir.text, "src":traducir.src, "dest":traducir.dest}
        
        return json.dumps(data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
