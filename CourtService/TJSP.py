'''
Created on Oct 25, 2014

@author: renato
'''
from CourtService.BaseService import BaseService
from CourtService import Credentials

class TJSP(BaseService):
    '''
    classdocs
    '''
    _USERNAME = Credentials.TJSP.get('username')
    _PASSWORD = Credentials.TJSP.get('password')
    _TOKEN_URL = 'http://esaj.tjsp.jus.br/sajcas/login'
    _LOGIN_URL = 'https://esaj.tjsp.jus.br/sajcas/login?username=%(user)s&password=%(pwd)s&lt=%(token)s&_eventId=submit&pbEntrar=Entrar&signature='
    _RETRIEVE_LAWSUIT_BY_ID_URL = 'https://esaj.tjsp.jus.br' \
                          '/cpo/pg/search.do?' \
                          'conversationId=&' \
                          'paginaConsulta=1&' \
                          'localPesquisa.cdLocal=-1&' \
                          'cbPesquisa=NUMPROC&' \
                          'tipoNuProcesso=UNIFICADO&' \
                          'numeroDigitoAnoUnificado=%(num_ano_unificado)s&' \
                          'foroNumeroUnificado=0037&' \
                          'dePesquisaNuUnificado=$(num_unificado)s&' \
                          'dePesquisaNuAntigo=&' \
                          'gateway=true'

    def __init__(self):
        '''
        Constructor
        '''
        BaseService.__init__(self)
        self._logged = False

    def getTokenURL(self):
        return self._TOKEN_URL

    def getLoginURL(self):
        return self._LOGIN_URL

    def getRetrieveLawsuitByIdURL(self):
        return self._RETRIEVE_LAWSUIT_BY_ID_URL

    def getToken(self):
        token_page = self.request_dispatcher.submitRequest(self.getTokenURL())
        return self.parser.getFromHTML(token_page, 'input', {'name': 'lt',})

    def getUsername(self):
        return self._USERNAME

    def getPassword(self):
        return self._PASSWORD

    def login(self):
        if not self._logged:
            login_details = {'user': self.getUsername(), 
                             'pwd': self.getPassword(), 
                             'token': self.getToken(),}
            self.request_dispatcher.submitRequest(self.getLoginURL(), 
                                                             login_details)
            self._logged = True

    def getLawsuitById(self, unified_year, lawsuit_id):
        self.login()
        query_details = {'num_ano_unificado': unified_year, 'num_unificado': lawsuit_id,}
        lawsuit_page = self.request_dispatcher.submitRequest(self.getRetrieveLawsuitByIdURL(), 
                                                             query_details)
        return self.parser.getFromHTML(lawsuit_page, 'div', {'id': 'listagemDeProcessos',})

# if __name__ == '__main__':
#     tjsp = TJSP()
#     print tjsp.getToken()
#     print tjsp.getLawsuitById('2014', '1')
