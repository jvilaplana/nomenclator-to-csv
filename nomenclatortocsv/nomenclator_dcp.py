from xml.etree import ElementTree
import csv
import os

def dcp():
    with open('data/DICCIONARIO_DCP.xml', 'rt') as f:
        tree = ElementTree.parse(f)

    root = tree.getroot()

    if not os.path.exists('csv'):
        os.makedirs('csv')

    with open('csv/DICCIONARIO_DCP.csv', 'wb') as csvfile:
        fieldnames = ['codigodcp', 'nombredcp', 'codigodcsa']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #writer.writeheader()

        for prescription in tree.findall('{http://schemas.aemps.es/prescripcion/aemps_prescripcion_dcp}dcp'):
            codigodcp = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion_dcp}codigodcp').text.encode('utf-8').strip()
            nombredcp = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion_dcp}nombredcp').text.encode('utf-8').strip()
            codigodcsa = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion_dcp}codigodcsa').text.encode('utf-8').strip()

            writer.writerow({'codigodcp': codigodcp, 'nombredcp': nombredcp, 'codigodcsa': codigodcsa})
