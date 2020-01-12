#!/usr/bin/env python3
from setuptools import setup

setup(name='discordbot',
      version='1.0.4',
      description='Bot Framework for Discord',
      author='DACRepair',
      author_email='DACRepair@gmail.com',
      url='https://github.com/CerberusGaming/discordbot-base',
      install_requires=[
          'discord.py',
          'sqlalchemy'
      ],
      packages=['discordbot',
                'discordbot.Common',
                'discordbot.Modules',
                'discordbot.Modules.Settings',
                'discordbot.Modules.Storage'])
