# coding: utf-8


def first_handler(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text='first',
    )


def second_handler(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text='second',
    )
