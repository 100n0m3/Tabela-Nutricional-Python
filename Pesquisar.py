#tabela nutricional
import requests,sys,re
from bs4 import BeautifulSoup

def pesquisar():
    pesquisa = input('Digite o que deseja pesquisar: ')
    with requests.Session() as s:
        requests.packages.urllib3.disable_warnings()
        page = s.post('http://www.tabelanutricional.com.br/pesquisa/'+pesquisa)
        soup = BeautifulSoup(page.text, 'html.parser')
        divs = soup.find_all("li", class_="cat-item")
        lista = {}
        v = 0
        print("Opcoes a pesquisar:")
        for item in divs:
            try:
                lista[v] = item.a["href"]
                print(v , item.text)
                v = v +1
            except:
                pass
        pesquisar = int(input("selecione a opcao desejada:"))
        q = lista[pesquisar]
        url = ('http://www.tabelanutricional.com.br'+q)
        page = s.post(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        resultado = soup.find_all("div", id="response")
        tabela = {}
        for item in resultado:
            linhas = item.findAll("td")
        print('Fruta Selecionada: ',re.sub(r"[^A-Za-z]+", ' ', q).upper())
        print('Nutrientes / Quantidade / % VD*')
        for a, b, c in zip(*[iter(linhas)]*3):
            print (a.text+" / ",    b.text+" / ",    c.text)

        pergunta()

def pergunta():  
    nova = input('DESEJA FAZER OUTRA PESQUISA? use S ou N para escolher')
    if nova == 'S':
        pesquisar()
    else:
        pass       
        
            
