# coding: utf-8
import telegram
import tornado.ioloop
import tornado.web

from bot.conf import BOT_TOKEN, WEBHOOK_URL
from bot.router import message_router


bot = telegram.Bot(token=BOT_TOKEN)


class IndexHandler(tornado.web.RequestHandler):

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        update = telegram.update.Update.de_json(data)
        message_router(bot, update)


class WebHookHandler(tornado.web.RequestHandler):

    def get(self):
        response = bot.setWebhook(WEBHOOK_URL)
        if not response:
            return self.write('Setting up webhook has failed')
        return self.write('Webhook has been successfully set')


def make_app():
    return tornado.web.Application([
        (r'/', IndexHandler),
        (r'/setwebhook', WebHookHandler)
    ])
