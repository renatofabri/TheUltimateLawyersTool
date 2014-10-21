'''
Created on Oct 20, 2014

@author: renato
'''

import requests
from bs4 import BeautifulSoup
from Common.LoginUrls import *
from Logins import LoginClient

class ParserTjSp:

    def __init__(self):
        print('')

    def parse_processo_by_numero(self, num_processo):

        loginClient = LoginClient()
        requester = loginClient.LoginTjSp(user='', pwd='')

        attrs = { 'num_unificado': num_processo, 'num_ano_unificado': num_processo }
        page = requester.get(TJSP_GET_PROCESSO_BY_NUMERO %  attrs, verify=False)

        pageSoup = BeautifulSoup(page.text)
        print pageSoup.prettify()



