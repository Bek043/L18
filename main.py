from telegram.ext import Updater , CommandHandler , MessageHandler , Filters
import logging 
import threading
updater = Updater(token='1833680648:AAFK9H1SMrMauWs65fTah6Ke2KHJDTbUiNg', use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

""" dispather способ на регагирование  """

dispatcher = updater.dispatcher 

""" Stop bot """
def shutdown():
    updater.stop()
    updater.is_idle = False

def stop(bot,update):
    threading.Thread(target=shutdown).start()


""" Command Execution """
""" /start """
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi . I am bot")

""" /info """
def info(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Infor")


""" Commands """

""" /start """
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

""" /info """
start_handler = CommandHandler('info', info)
dispatcher.add_handler(start_handler)

""" Messages execution """

def privet(update, context):
    msg = update.message.text 
    if "privet" in msg:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Privet i tebe.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

""" New user execution """

def newuser(update, context ):
    if update.message.new_chat_members:
        user = update.message.new_chat_members[0]
        context.bot.send_message(chat_id=update.effective_chat.id, text="Privet" + user ["username"])

""" Messages """
privet_handler = MessageHandler(Filters.text , privet )
dispatcher.add_handler(privet_handler)

""" New user Handler """
newuser_handler = MessageHandler(Filters.status_update.new_chat_members , newuser )
updater.dispatcher.add_handler(newuser_handler)


""" Stop bot """
updater.dispatcher.add_handler(CommandHandler("stop" , stop))

""" Старт бота """

updater.start_polling()

print("Bot started")


