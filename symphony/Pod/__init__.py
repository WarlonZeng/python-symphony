#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Pod API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


import symphonybinding

from .users import Users
from .streams import Streams
from .groups import Groups
from .connections import Connections
from .admin import Admin
from .base import Base


class Pod(Base, Users, Streams, Groups, Connections, Admin):

    def __init__(self, url, session, keymngr):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        try:
            CG = symphonybinding.SymCodegen()
            self.__pod__ = CG.pod_cg(self.__url__)
        except Exception as err:
            print (err)
