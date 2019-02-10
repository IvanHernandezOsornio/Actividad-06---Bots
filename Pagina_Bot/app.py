import web
        
urls = (
    '/', 'application.controllers.instrumentos.index.Index',
    '/insert', 'application.controllers.instrumentos.insert.Insert',
    '/update/(.*)', 'application.controllers.instrumentos.update.Update',
    '/delete/(.*)', 'application.controllers.instrumentos.delete.Delete',
    '/view/(.*)', 'application.controllers.instrumentos.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
