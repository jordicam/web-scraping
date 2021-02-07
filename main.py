####IMPORTS
import requests
from bs4 import BeautifulSoup
import pandas as pd



#####DEF
def main():
    pais_capital = {} 
    r = requests.get('https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses')
    soup = BeautifulSoup(r.text, 'lxml')
    tables = soup.find_all("table")
    first_table = tables[0]
    fila = first_table.find("tbody")
    trs = fila.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) == 9:
            pais = tds[1].text.strip("\n")
            capital = tds[3].text.strip("\n")
            #{key:value, key2: value2}
            pais_capital[pais] =  capital
    df = pd.DataFrame(pais_capital.items(), columns=['Pais', 'Capital'])
    df.to_excel("pais_capital.xls")






####EJECUCION
if __name__ == "__main__":
    main()


