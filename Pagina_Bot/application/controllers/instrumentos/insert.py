import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # alamcena el nombre escrito en el input
        marca = formulario['marca'] 
        modelo = formulario['modelo'] # alamcena el nombre escrito en el input
        color = formulario['color']# almacena el email escrito en el input
        config.model_instrumentos.insert_instrumentos(nombre, marca, modelo, color) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
