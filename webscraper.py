# -*- coding: utf-8 -*-
'''
Esse módulo é responsável por obter o código fonte do HTML necessário para posterior análise.


Descrição detalhada
-------------
Sem descrição detalhada ainda 


'''

# Base python imports:
# import 

# Third-party libs:
import requests
from bs4 import BeautifulSoup

# Recebe o input do form no front e armazena o link a ser analisado:
input_from_front = 'https://www.testurl.com/home.html'

# Faz a requisição do código fonte em html:
htmlpage = requests.get(input_from_front)

# Obj da lib Soup para análise:
bsoup = BeautifulSoup(htmlpage.text, 'html.parser')

#TODO:
# ver a WCAG e procurar uma api para analisar o HTML.
# na falta de uma api (díficil), analisar o html por tags.





