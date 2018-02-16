#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: Daniel L.J.
# E-mail: daniellessa.j@gmail.com

from bs4 import BeautifulSoup
import requests

def GetFullAddressByZipCodeOnBrazil(zipcode):
    '''
    Passa como valor de entrada um CEP (string), onde o mesmo é consultado no site dos correios. A saída é através de uma
    lista com as informações do CEP consultado: 'Logradouro/Nome','Bairro/Distrito','Cidade', 'Estado','CEP'.
    '''
    resp=None
    htmltable=None
    listainfo=[]
    
    if (isinstance(zipcode, str) and len(zipcode)==8 and zipcode is not None): #veriifcações iniciais
        urlconsulta = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
        carga = {'relaxation': zipcode, 'tipoCEP': 'ALL', 'semelhante': 'N'}
        resp = requests.post(urlconsulta, data=carga)
    
    if resp is not None:
        if resp.status_code != 200: #Verifica qualquer evento de erro durante acesso com método post
            raise Exception("Falha no acesso ao site dos correios.", resp.status_code)
        else:
            #soup = BeautifulSoup(resp.text, "html.parser")
            tables = BeautifulSoup(resp.text, "lxml").find_all("table")
    
            for table in tables:
                if table.find_parent("table", attrs={'class': 'tmptabela'}) is None:  # buscando somente "tables" no HTML
                    htmltable = table
            if htmltable is not None:
                i = 1 # iterador
                for td in htmltable.find_all("td"):
                    if (i==3): #Trata-se da Cidade
                        posicao = ((td.text).index("/")) + 1
                        listainfo.append(str(td.text[:-3]).strip())
                        listainfo.append(str(td.text[posicao:]).strip())
                    elif (i==4): #Trata-se do CEP
                        listainfo.append((str(td.text).replace("-","").strip()).rjust(8,'0'))
                    else:
                        listainfo.append(str(td.text.strip()))
                    if (i % 4 != 0):
                        i = i + 1

                return listainfo #visualiza