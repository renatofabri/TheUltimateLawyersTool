__author__ = 'Fn'

import requests
from bs4 import BeautifulSoup
from Common.LoginUrls import TJSP_TOKEN_URL, TJSP_LOGIN_URL


class LoginClient:

    def LoginTjSp(self, user, pwd):


        try:
            #Creating a requests.Session() object. It can hold cookies and session
            #infos, so we can generate a token and use it into the same session
            s = requests.Session()
            #Setting User-Agent to be a Browser-Like request
            s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

            #Getting the page content
            content = s.get(TJSP_TOKEN_URL)
            #Parsing it
            soup = BeautifulSoup(content.text)
            #And finally getting the token
            token = soup.find("input", {"name": "lt"})['value']

            #Setting the GET parameters
            #attrs = {'user': '33812315882', 'pwd': 'pedro12k14', 'token': token}
            attrs = {'user': user, 'pwd': pwd, 'token': token}
            #Requesting the page. verify=False means that we're ignoring the SSL server
            s.get(TJSP_LOGIN_URL % attrs, verify=False)

            if s == 200:
                return s

        except Exception, e:
            raise e

