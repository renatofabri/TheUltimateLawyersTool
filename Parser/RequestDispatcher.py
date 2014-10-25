'''
Created on Oct 25, 2014

@author: renato
'''
import requests

class RequestDispatcher(object):
    '''
    classdocs
    '''

    DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    def __init__(self):
        '''
        Constructor of class RequestDispatcher
        This constructor method will create a new Request Session
        '''
        self.session = requests.Session();
        self.session.headers['User-Agent'] = self.DEFAULT_USER_AGENT

    def submitRequest(self, url, data={}, verify_ssh=False):
        '''
        This method will make a call to the url using the given data
        @param url: the URL that will be called
        @param data: the data that will be used in the URL call
        @param verifySSH: optional parameter, defines if SSH will be verified
        @return: A string containing the HTML of the requested page
        
        '''
        if data:
            response = self.session.get(url % data, verify=verify_ssh)
        else:
            response = self.session.get(url, verify=verify_ssh)

        return response.text
