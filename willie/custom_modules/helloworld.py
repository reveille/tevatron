"""
helloworld.py : A willie tutorial callable

Remember to say .helloworld
"""

import willie
@willie.module.commands('helloworld')

def helloworld(bot, trigger):
   bot.say('You and your world can go get fucked')

