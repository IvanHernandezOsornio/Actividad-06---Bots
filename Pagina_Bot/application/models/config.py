import web
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'music18',
    user = 'music',
    pw = 'music.2019',
    port = 3306
    )