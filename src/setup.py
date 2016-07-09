# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='telegram_tornado',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bot_polling = bot.main:polling_run',
            'bot_webhook = bot.main:webhook_run',
        ]
    },
)
