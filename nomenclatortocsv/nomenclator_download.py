import urllib
import zipfile
import os


def download():
    if os.path.isdir("data") == True:
        print "data directory already exists, exiting ..."
        return -1
    
    nomenclator = urllib.URLopener()
    nomenclator.retrieve("http://listadomedicamentos.aemps.gob.es/prescripcion.zip", "nomenclator.zip")

    zip_ref = zipfile.ZipFile("nomenclator.zip", 'r')
    zip_ref.extractall("data")
    zip_ref.close()

    os.remove("nomenclator.zip")
