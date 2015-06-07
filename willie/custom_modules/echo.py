from willie import module

@module.commands('echo')
def echo(bot, trigger):
    bot.reply(trigger.group(2))
