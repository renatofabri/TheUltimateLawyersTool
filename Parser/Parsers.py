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
        requester = loginClient.LoginTjSp(user='33812315882', pwd='pedro12k14')

        attrs = { 'num_unificado': num_processo, 'num_ano_unificado': '' }
        page = requester.get(TJSP_GET_PROCESSO_BY_NUMERO %  attrs, verify=False)

        pageSoup = BeautifulSoup(page.text)
        print pageSoup.prettify()



