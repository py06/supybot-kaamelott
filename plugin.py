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
import random



class Kaamelott(callbacks.Plugin):
    """Quote from Kaamelott """
    pass

    def __init__(self, irc):
        self.__parent = super(Kaamelott, self)
        self.__parent.__init__(irc)
        self.rng = random.Random()   # create our rng
        self.rng.seed()   # automatically seeds with current time
        self.data = "/home/pkerbrat/supybot/plugins/Kaamelott/kaamelott"

    def citation(self, irc, msg, args):
        recueil = []
        j = 1
        quote = [] 
        picked = [] 
        srcfile = open(self.data, 'r')
        for line in srcfile:
            if (line.startswith("%")):
                recueil.append(quote[:])
                quote = []
            else:
                quote.append(unicode(line.rstrip(), "utf-8"))
        picked = random.choice(recueil)
        for line in picked:
            irc.reply(line.encode("utf-8", "replace"), prefixNick=False)

    citation = wrap(citation)

Class = Kaamelott


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
