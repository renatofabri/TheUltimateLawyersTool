import requests
from bs4 import BeautifulSoup

TOKEN_URL = 'http://esaj.tjsp.jus.br/sajcas/login'
LOGIN_URL = 'https://esaj.tjsp.jus.br/sajcas/login?username=%(user)s&password=%(pwd)s&lt=%(token)s&_eventId=submit&pbEntrar=Entrar&signature='

TEST_URL = 'https://esaj.tjsp.jus.br/cpo/pg/search.do?conversationId=&paginaConsulta=1&localPesquisa.cdLocal=-1&cbPesquisa=NUMPROC&tipoNuProcesso=UNIFICADO&numeroDigitoAnoUnificado=0014414-38.2013&foroNumeroUnificado=0037&dePesquisaNuUnificado=0014414-38.2013.8.26.0037&dePesquisaNuAntigo=&gateway=true'

#Creating a requests.Session() object. It can hold cookies and session
#infos, so we can generate a token and use it into the same session
s = requests.Session()
#Setting User-Agent to be a Browser-Like request
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

#Getting the page content
content = s.get(TOKEN_URL)
#Parsing it
soup = BeautifulSoup(content.text)
#And finally getting the token
token = soup.find("input", {"name": "lt"})['value']

#Setting the GET parameters
attrs = {'user': '33812315882', 'pwd': 'pedro12k14', 'token': token}
#Requesting the page. verify=False means that we're ignoring the SSL server
login = s.get(LOGIN_URL % attrs, verify=False)

teste = s.get(TEST_URL, verify=False)
soupTeste = BeautifulSoup(teste.text)
print soupTeste.prettify()



