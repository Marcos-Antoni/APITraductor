from flask import Blueprint, request
# from src.classTranslator import ClassTranslator, listar_idiomas

main = Blueprint('main', __name__) 

@main.route('/')
def index():
    from src.classTranslator import ClassTranslator
    
    src = request.args.get('src', "")
    dest = request.args.get('dest', "")
    text = request.args.get('text', "")
    
    obj_traductor = ClassTranslator(src, dest)
    traduccion = obj_traductor.traducir(text)
    
    if "error" in traduccion:
        return traduccion, 400
    
    
    return traduccion    

@main.route('/listaLanguages')
def listaLanguages():
    from src.classTranslator import listar_idiomas

    return listar_idiomas()
    