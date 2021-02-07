import requests
from bs4 import BeautifulSoup
import pandas as pd
from os.path  import basename


def get_html(enlace):
    r = requests.get(enlace)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

def downloadimages(soup, nimg=-1):
    imagenes_desc = []
    myimg = soup.findAll("img")
    for link in myimg[0:nimg]:
        name_imagen_desc = descargarimagen(link)
        imagenes_desc.append(name_imagen_desc)
    return imagenes_desc


def downloadimages_url(enlace,nimg):
    soup = get_html(enlace)
    imagenes_desc = downloadimages(soup, nimg)
    return imagenes_desc




def descargarimagen(link):
    lnk = link.get('src')
    lnk= "https:" + lnk
    name_imagen_des = basename(lnk)
    with open(name_imagen_des, "wb") as f:
        f.write(requests.get(lnk).content)
    return name_imagen_des