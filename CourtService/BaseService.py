'''
Created on Oct 25, 2014

@author: renato
'''
from Parser.RequestDispatcher import RequestDispatcher
from Parser.Parser import Parser

class BaseService(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.request_dispatcher = RequestDispatcher()
        self.parser = Parser()
