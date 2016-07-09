# coding: utf-8
import os

from bot.tornado_app import make_app


def webhook_run():
    import tornado.ioloop
    import tornado.web
    from tornado.options import options

    options.logging = 'debug'

    app = make_app()
    app.listen(int(os.environ.get('PORT', '5000')))
    tornado.ioloop.IOLoop.current().start()


def polling_run():
    from telegram import ext
    from bot.conf import BOT_TOKEN
    from bot.router import first_handler, second_handler

    updater = ext.Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(ext.MessageHandler([ext.Filters.text], first_handler))
    dp.add_handler(ext.MessageHandler([ext.Filters.text], second_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    polling_run()
