from webscraping.main import descargarimagen, downloadimages_url
from bs4 import BeautifulSoup
import requests
import os
import glob



def test_descargarimagen():
    r = requests.get("https://es.wikipedia.org/wiki/Anexo:Municipios_de_Espa%C3%B1a_por_poblaci%C3%B3n")
    soup = BeautifulSoup(r.text, 'lxml')
    myimg = soup.findAll("img")[0]
    descargarimagen(myimg)
    assert os.path.exists("400px-Municipalities_of_Spain.svg.png") == True


def test_main():
    pngs = glob.glob("*.png")
    for png in pngs:
        os.remove(png)
    enlace = "https://es.wikipedia.org/wiki/Anexo:Municipios_de_Espa%C3%B1a_por_poblaci%C3%B3n"
    nimg = 4
    imagenes_desc = downloadimages_url(enlace,nimg)
    for img in imagenes_desc:
        assert os.path.exists(img) == True
    assert len(imagenes_desc) == nimg



    