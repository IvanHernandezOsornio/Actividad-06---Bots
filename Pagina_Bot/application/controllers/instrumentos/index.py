import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        instrumentos = config.model_instrumentos.select_instrumentos().list() 
        return config.render.index(instrumentos) # Envia todos los registros y renderiza index.html
