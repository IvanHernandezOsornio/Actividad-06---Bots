import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        instrumentos = config.model_instrumentos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(instrumentos) # Envia el registro y renderiza update.html
    
    def POST(self, marca):
        formulario = web.input() # almacena los datos del formulario web
        nombre = formulario['nombre'] # almacena el nombre del input email
        marca = formulario['marca']
        modelo = formulario['modelo']
        color = formulario['color']# almacena el email del input password
        config.model_instrumentos.update_instrumentos(nombre, marca, modelo, color) # actuliza los valores
        raise web.seeother('/') # redirecciona al index
