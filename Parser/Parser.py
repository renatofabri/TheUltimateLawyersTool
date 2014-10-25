'''
Created on Oct 25, 2014

@author: renato
'''
from bs4 import BeautifulSoup

class Parser(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def getFromHTML(self, html, field_type, field_attrs):
        '''
        TODO: add method description
        '''
        soup_instance = BeautifulSoup(html)
        requested_field = soup_instance.find(field_type, field_attrs)
        try:
            return requested_field['value']
        except KeyError:
            pass
        return requested_field

    def getCompleteHTML(self, html):
        '''
        TODO: add method description
        '''
        soup_instance = BeautifulSoup(html)
        return soup_instance
