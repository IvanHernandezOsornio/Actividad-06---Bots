import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla persornas
'''
def select_instrumentos():
    try:
        return db.select('instrumentos') # Selecciona todos los registros de la tabla 
    except Exception as e:
        print "Model select_instrumentos Error {}".format(e.args)
        print "Model select_instrumentos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_nombre(nombre):
    try:
        return db.select('instrumentos',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando nombre y email
'''
def insert_instrumentos(nombre, marca, modelo, color):
    try:
        return db.insert('instrumentos', nombre=nombre,marca=marca,modelo=modelo,color=color) # inserta un registro en 
    except Exception as e:
        print "Model insert_instrumentos Error {}".format(e.args)
        print "Model insert_instrumentos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_instrumentos(nombre):
    try:
        return db.delete('instrumentos', where='nombre=$nombre',vars=locals()) # borra un registro de 
    except Exception as e:
        print "Model delete_instrumentos Error {}".format(e.args)
        print "Model delete_instrumentos Message {}".format(e.message)
        return None

'''
Metodo para actualizar el email, del nombre recibido
'''
def update_instrumentos(nombre, marca, modelo, color): 
    try:
        return db.update('instrumentos', 
            marca=marca, 
            modelo=modelo, 
            color=color,                          
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_instrumentos Error {}".format(e.args)
        print "Model update_instrumentos Message {}".format(e.message)
        return None
