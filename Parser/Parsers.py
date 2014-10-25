'''
Created on Oct 20, 2014

@author: renato
'''

from bs4 import BeautifulSoup
from Common.LoginUrls import TJSP_GET_PROCESSO_BY_NUMERO, TJSP_TOKEN_URL,\
    TJSP_LOGIN_URL
from Logins import LoginClient
import requests

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



if __name__ == '__main__':
    session = requests.Session()
    #Setting User-Agent to be a Browser-Like request
    session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    #Getting the page content
    content = session.get(TJSP_TOKEN_URL)
    #Parsing it
    soup = BeautifulSoup(content.text)
    #And finally getting the token
    token = soup.find("input", {"name": "lt"})['value']

    #Setting the GET parameters
    attrs = {'user': '33812315882', 'pwd': 'pedro12k14', 'token': token}
    #Requesting the page. verify=False means that we're ignoring the SSL server
    session.get(TJSP_LOGIN_URL % attrs, verify=False)

    attrs = { 'num_unificado': '', 'num_ano_unificado': '' }

    page = session.get(TJSP_GET_PROCESSO_BY_NUMERO %  attrs, verify=False)

    pageSoup = BeautifulSoup(page.text)

    print pageSoup