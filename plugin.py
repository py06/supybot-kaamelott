# -*- coding: utf-8 -*-
###
# Copyright (c) 2016, Pierre-Yves Kerbrat
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DIKaamelottLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.conf as conf
import random
import os

class Kaamelott(callbacks.Plugin):
    """Quote from Kaamelott """
    pass

    def __init__(self, irc):
        self.__parent = super(Kaamelott, self)
        self.__parent.__init__(irc)
        self.rng = random.Random()   # create our rng
        self.rng.seed()   # automatically seeds with current time
	self.count = 0 #reset global counter
	self.nextreply = self.rng.randint(1, 10) # when coun reach this value then bot replies
	self.log.info("count={} next={}".format(self.count, self.nextreply))
        self.messages = ["C'est pas faux", "Je vous piche de mieux en mieux",\
                "Entre 7 et 26, a 3 j'ai rien piche, a 13 je suis pas sur et a 17 j'ai tout compris"]

    def invalidCommand(self, irc, msg, tokens):
        try:
            self.log.debug('Channel is: "+str(irc.isChannel(msg.args[0]))')
            self.log.debug("Message is: "+str(msg.args))
        except:
            self.log.error("message not retrievable.")

        if not irc.isChannel(msg.args[0]):
            channel = msg.args[0]
	    self.count = self.count + 1
	    if self.nextreply == self.count:
		    self.count = 0
		    self.nextreply = self.rng.randint(1, 10)
                    randmsg = self.rng.randint(0, len(self.messages)-1)
		    reply = self.messages[randmsg]
                    self.log.debug("Reply is: "+str(reply))
                    irc.reply(reply)

    def citation(self, irc, msg, args):
        recueil = []
        j = 1
        quote = [] 
        picked = [] 
        filename = self.registryValue('quotes')
        if not filename:
            self.log.error("Please provide path to quotes in config")
            self.log.error("add supybot.plugins.Kaamelott.quotes")
            irc.error("quotes not installed", Raise=True)


        if os.path.exists(filename):
            with open(filename, 'r') as srcfile:
                try:
                    # do stuff
                    for line in srcfile:
                        if (line.startswith("%")):
                            recueil.append(quote[:])
                            quote = []
                        else:
                            quote.append(unicode(line.rstrip(), "utf-8"))
                    picked = random.choice(recueil)
                    for line in picked:
                        irc.reply(line.encode("utf-8", "replace"), prefixNick=False)
                except : # whatever reader errors you care about
                    # handle error
                    self.log.error("Could not open quotes file")
                    irc.error(_("Could not open quotes file"), Raise=True)
        else:
            self.log.error("unknow file: {}".format(filename))

    citation = wrap(citation)

Class = Kaamelott


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
