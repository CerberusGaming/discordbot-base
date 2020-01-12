#!/usr/bin/env python3
from setuptools import setup

setup(name='discordbot',
      version='1.0.2',
      description='Bot Framework for Discord',
      author='DACRepair',
      author_email='DACRepair@gmail.com',
      url='https://github.com/CerberusGaming/discordbot-base',
      install_requires=[
          'discord.py',
          'sqlalchemy'
      ],
      packages=['discordbot_base',
                'discordbot_base.Common',
                'discordbot_base.Modules',
                'discordbot_base.Modules.Settings',
                'discordbot_base.Modules.Storage'])
