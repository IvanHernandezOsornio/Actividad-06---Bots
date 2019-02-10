from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging 
import web


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'music18',
    user = 'music',
    pw = 'music.2019',
    port = 3306
    )

token = '679596840:AAH0RI58JnnTovI_Y0xZNrvqTT549C4hpOQ'             #Coneccion con SpitirOfFirebot
         
def start(bot, update):
    username = update.message.from_user.username 
    update.message.reply_text('Hola {} Cual es tu instrumento indicado\nUsa el comando:/nombre' .format(username))

def help(bot, update):
    username = update.message.from_user.username 
    update.message.reply_text('Hola {} Cual es tu instrumento indicado\nUsa el comando:/nombre'.format(username))

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        nombre = int(text[1]) 
        print "Send info to {}".format(username)
        print "Key search {}".format(nombre)
        result = db.select('instrumentos', where='nombre=$nombre', vars=locals())[0]
        print result
        respuesta =  "Nombre: " + str(result.nombre) + "\nMarca: " + str(result.marca) + "\nModelo: " + str(result.modelo) + "\nColor: " + str(result.color)
        update.message.reply_text('Hola {}Tu instrumento es:\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(nombre))

def info(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'MusicBot'
        
        updater = Updater(token)


        dp = updater.dispatcher

        print 'Listo :v'
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("nombre", info))        


        dp.add_handler(MessageHandler(Filters.text, echo))


        dp.add_error_handler(error)


        updater.start_polling()


        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
