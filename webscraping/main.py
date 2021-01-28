####IMPORTS
import requests
from bs4 import BeautifulSoup
import pandas as pd
from os.path  import basename
import argparse


def leer_inputs():
    parser = argparse.ArgumentParser(description='Descarga todas las imagnes de tu url preferida!')
    parser.add_argument('--url', type=str, help='Pon tu url a descargar las imagines i.e --url www.wikipedia.com')
    parser.add_argument('--nimg', type=int, help='Pon el número de imágenes a descargar')
    args = parser.parse_args()
    return args.url, args.nimg


def main(enlace, nimg):
    #selenium
    imagenes_desc = []
    r = requests.get(enlace)
    soup = BeautifulSoup(r.text, 'lxml')
    myimg = soup.findAll("img")
    for link in myimg[0:nimg]:
        print(link)
        name_imagen_desc = descargarimagen(link)
        imagenes_desc.append(name_imagen_desc)
    return imagenes_desc

def descargarimagen(link):
    lnk = link.get('src')
    lnk= "https:" + lnk
    name_imagen_des = basename(lnk)
    with open(name_imagen_des, "wb") as f:
        f.write(requests.get(lnk).content)
    return name_imagen_des
    
    



####EJECUCION
if __name__ == "__main__":
    ##INPUT SIEMPRE SACA UNA STRING
    enlace, nimg = leer_inputs()
    main(enlace, nimg)