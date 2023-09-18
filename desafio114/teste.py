import urllib
import urllib.request

link = 'http://www.pudim.com.br/'
try:
    site = urllib.request.urlopen(link)
except urllib.request.URLError:
    print('erro')
else:
    print(f'O site {link} está disponível no momento.')