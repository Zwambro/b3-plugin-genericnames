
__version__ = '1.0'
__author__ = 'Zwambro'

import b3
import b3.events
import b3.plugin
from b3 import functions
import re

class GenericnamesPlugin(b3.plugin.Plugin):
    _adminPlugin = False
    requiresConfigFile = False
    _GenericNames = ["^Unknown", "VickNet", "CHEATER"]


    def onStartup(self):

        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.debug('Could not find admin plugin')
            return False
        else:
            self.debug('Plugin loaded normal')
        self.registerEvent(b3.events.EVT_CLIENT_AUTH)
        self.debug('Started')

    def onEvent(self, event):
        if event.type == b3.events.EVT_CLIENT_AUTH:
            client = event.client
            for x in self._GenericNames:
                if re.match(x, client.name):
                    self.debug("Kicking %s because his name is generic name" %(event.client.exactName))
                    client.kick("^1Warning: ^7Change your name by typing ^1/name^7 on your console or ask for help on ^3@forum.plutonium.pw^7")
                    return 
                else:
                    self.debug("%s don't have generic name" %(client.name))
                return
