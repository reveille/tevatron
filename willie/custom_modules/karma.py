## 
# Karma for Willie by Rev
#
# These fake IRC logs are examples of what the functions should look like.
# 
#
#
# <mik3> .karma
#
# <Tevatron> Here's the Karma top 10 list:
# <Tevatron>
# <Tevatron> 1. Chicago (582)
# <Tevatron> 2. beer (41)
# <Tevatron> 3. weed (37)
# <Tevatron> 4. PORN! (32)
# <Tevatron> 5. tacos (28)
# <Tevatron> 6. boobs (23)
# <Tevatron> 7. Linux (19)
# <Tevatron> 8. coffee (14)
# <Tevatron> 9. cycling (7)
# <Tevatron> 10. IRC (5)
#
#
#
# <mik3> .karma +beer
# <Tevatron> beer (42)
#
# <mik3> .karma -beer
# <Tevatron> beer (41)
#
# <mik3> .karmawhore 
# <Tevatron> %s is the top karma-whore, with %s up/downvotes. % (somenick, somenumber)

from willie import *
from collections import Counter
import re
import os

dbfile = os.path.dirname(os.path.realpath(__file__)) + '/karma.db'

def timestamp():
    lt = time.localtime(time.time())
    return "%02d.%02d.%04d %02d:%02d:%02d" % (lt[2], lt[1], lt[0], lt[3], lt[4], lt[5])


@module.commands('karma')
@module.example('.karma')
def peakusers(bot, trigger):
    f = open(dbfile, 'r')
    count = f.read()
    bot.reply("The most meatbags I've seen were %s here, give or take a few superior beings like me." % count)

