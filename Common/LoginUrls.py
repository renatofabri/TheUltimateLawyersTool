__author__ = 'Fn'

TJSP_TOKEN_URL = 'http://esaj.tjsp.jus.br/sajcas/login'
TJSP_LOGIN_URL = 'https://esaj.tjsp.jus.br/sajcas/login?username=%(user)s&password=%(pwd)s&lt=%(token)s&_eventId=submit&pbEntrar=Entrar&signature='
TJSP_GET_PROCESSO_BY_NUMERO = 'https://esaj.tjsp.jus.br' \
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
