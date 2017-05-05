from xml.etree import ElementTree
import csv
import os

def prescripcion():
    with open('data/Prescripcion.xml', 'rt') as f:
        tree = ElementTree.parse(f)

    root = tree.getroot()

    if not os.path.exists('csv'):
        os.makedirs('csv')

    with open('csv/Prescripcion.csv', 'wb') as csvfile:
        fieldnames = ['cod_nacion', 'nro_definitivo', 'des_nomco', 'des_prese', 'cod_dcsa', 'cod_dcp', 'cod_dcpf', 'des_dosific', 'cod_envase', 'contenido', 'unid_contenido', 'nro_conte', 'sw_psicotropo', 'sw_estupefaciente', 'sw_afecta_conduccion', 'sw_triangulo_negro', 'url_fictec', 'url_prosp', 'sw_receta', 'sw_generico', 'sw_sustituible', 'sw_envase_clinico', 'sw_uso_hospitalario', 'sw_diagnostico_hospitalario', 'sw_tld', 'sw_especial_control_medico', 'sw_huerfano', 'sw_base_a_plantas', 'laboratorio_titular', 'laboratorio_comercializador', 'fecha_autorizacion', 'sw_comercializado', 'fec_comer', 'cod_sitreg', 'cod_sitreg_presen', 'fecha_situacion_registro', 'fec_sitreg_presen', 'sw_tiene_excipientes_decl_obligatoria', 'biosimilar', 'importacion_paralela']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #writer.writeheader()

        for prescription in tree.findall('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}prescription'):
            cod_nacion = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_nacion').text.encode('utf-8').strip()
            nro_definitivo = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}nro_definitivo').text.encode('utf-8').strip()
            des_nomco = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}des_nomco').text.encode('utf-8').strip()
            des_prese = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}des_prese').text.encode('utf-8').strip()

            cod_dcsa = ""
            if prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_dcsa') is not None:
                cod_dcsa = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_dcsa').text.encode('utf-8').strip()

            cod_dcp = ""
            if prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_dcp') is not None:
                cod_dcp = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_dcp').text.encode('utf-8').strip()

            cod_dcpf = ""
            if prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_dcpf') is not None:
                cod_dcpf = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_dcpf').text.encode('utf-8').strip()

            des_dosific = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}des_dosific').text.encode('utf-8').strip()
            cod_envase = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_envase').text.encode('utf-8').strip()

            contenido = ""
            if prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}contenido') is not None:
                contenido = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}contenido').text.encode('utf-8').strip()

            unid_contenido = ""
            if prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}unid_contenido') is not None:
                unid_contenido = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}unid_contenido').text.encode('utf-8').strip()

            nro_conte = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}nro_conte').text.encode('utf-8').strip()
            sw_psicotropo = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_psicotropo').text.encode('utf-8').strip()
            sw_estupefaciente = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_estupefaciente').text.encode('utf-8').strip()
            sw_afecta_conduccion = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_afecta_conduccion').text.encode('utf-8').strip()
            sw_triangulo_negro = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_triangulo_negro').text.encode('utf-8').strip()
            url_fictec = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}url_fictec').text.encode('utf-8').strip()
            url_prosp = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}url_prosp').text.encode('utf-8').strip()
            sw_receta = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_receta').text.encode('utf-8').strip()
            sw_generico = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_generico').text.encode('utf-8').strip()
            sw_sustituible = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_sustituible').text.encode('utf-8').strip()
            sw_envase_clinico = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_envase_clinico').text.encode('utf-8').strip()
            sw_uso_hospitalario = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_uso_hospitalario').text.encode('utf-8').strip()
            sw_diagnostico_hospitalario = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_diagnostico_hospitalario').text.encode('utf-8').strip()
            sw_tld = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_tld').text.encode('utf-8').strip()
            sw_especial_control_medico = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_especial_control_medico').text.encode('utf-8').strip()
            sw_huerfano = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_huerfano').text.encode('utf-8').strip()
            sw_base_a_plantas = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_base_a_plantas').text.encode('utf-8').strip()
            laboratorio_titular = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}laboratorio_titular').text.encode('utf-8').strip()
            laboratorio_comercializador = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}laboratorio_comercializador').text.encode('utf-8').strip()
            fecha_autorizacion = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}fecha_autorizacion').text.encode('utf-8').strip()
            sw_comercializado = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_comercializado').text.encode('utf-8').strip()
            fec_comer = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}fec_comer').text.encode('utf-8').strip()
            cod_sitreg = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_sitreg').text.encode('utf-8').strip()
            cod_sitreg_presen = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}cod_sitreg_presen').text.encode('utf-8').strip()
            fecha_situacion_registro = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}fecha_situacion_registro').text.encode('utf-8').strip()
            fec_sitreg_presen = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}fec_sitreg_presen').text.encode('utf-8').strip()
            sw_tiene_excipientes_decl_obligatoria = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}sw_tiene_excipientes_decl_obligatoria').text.encode('utf-8').strip()
            biosimilar = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}biosimilar').text.encode('utf-8').strip()
            importacion_paralela = prescription.find('{http://schemas.aemps.es/prescripcion/aemps_prescripcion}importacion_paralela').text.encode('utf-8').strip()

            writer.writerow({'cod_nacion': cod_nacion, 'nro_definitivo': nro_definitivo, 'des_nomco': des_nomco, 'des_prese': des_prese, 'cod_dcsa': cod_dcsa, 'cod_dcp': cod_dcp, 'cod_dcpf': cod_dcpf, 'des_dosific': des_dosific, 'cod_envase': cod_envase, 'contenido': contenido, 'unid_contenido': unid_contenido, 'nro_conte': nro_conte, 'sw_psicotropo': sw_psicotropo, 'sw_estupefaciente': sw_estupefaciente, 'sw_afecta_conduccion': sw_afecta_conduccion, 'sw_triangulo_negro': sw_triangulo_negro, 'url_fictec': url_fictec, 'url_prosp': url_prosp, 'sw_receta': sw_receta, 'sw_generico': sw_generico, 'sw_sustituible': sw_sustituible, 'sw_envase_clinico': sw_envase_clinico, 'sw_uso_hospitalario': sw_uso_hospitalario, 'sw_diagnostico_hospitalario': sw_diagnostico_hospitalario, 'sw_tld': sw_tld, 'sw_especial_control_medico': sw_especial_control_medico, 'sw_huerfano': sw_huerfano, 'sw_base_a_plantas': sw_base_a_plantas, 'laboratorio_titular': laboratorio_titular, 'laboratorio_comercializador': laboratorio_comercializador, 'fecha_autorizacion': fecha_autorizacion, 'sw_comercializado': sw_comercializado, 'fec_comer': fec_comer, 'cod_sitreg': cod_sitreg, 'cod_sitreg_presen': cod_sitreg_presen, 'fecha_situacion_registro': fecha_situacion_registro, 'fec_sitreg_presen': fec_sitreg_presen, 'sw_tiene_excipientes_decl_obligatoria': sw_tiene_excipientes_decl_obligatoria, 'biosimilar': biosimilar, 'importacion_paralela': importacion_paralela})
