# coding: utf-8
from bot.handlers import first_handler, second_handler


def message_router(bot, update):
    if update.message.text == '1':
        first_handler(bot, update)

    elif update.message.text == '2':
        second_handler(bot, update)

    else:
        bot.sendMessage(
            chat_id=update.message.chat_id,
            text='nothing',
        )
