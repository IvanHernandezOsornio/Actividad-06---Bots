import web # importa la libreria web.py
import application.models.model_instrumentos as model_instrumentos


render = web.template.render('application/views/instrumentos/', base='master') # configura la ubicacion de las vistas