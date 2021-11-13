import requests
import argparse
from virus_total_apis import PrivateApi
from openpyxl import Workbook

"""def xlsx():
        i = 1
        Links = []
        book = Workbook()
        sheet = book.active
        sheet['A1'] = "URL"
        sheet['B1'] = "Fecha de análisis"
        sheet['C1'] = "Total de análisis"
        sheet['D1'] = "Análisis positivos"
        sheet['E1'] = "Clasificación"
        while i == 1 :
            link = input("Ingrese un link: ")
            Links.append(link)
            i = int(input("Ingrese un 1 para seguir agregando, "
                          "de lo contrario cualquier otro numero: "))
        with open('urls_sospechosas.txt', 'w') as temp_file:
            for item in Links:
                temp_file.write("%s\n" % item)

def api():
    API_KEY = "7ba043588bf8968632f5d560ad47e1438bfd36991a676ae4bbe0f179bd0fba32"
    api = PrivateApi(API_KEY)

def libro():
    z = 1
    with open ("urls_sospechosas.txt", "r") as file:
        for line in file:
            response = api.get_url_report(line)
            filtro = {'results':response['results']}
            filtro2 = filtro.get('results')
            z = int(z)
            z = z + 1
            z = str(z)
            valor1 = 'A' + z
            valor2 = 'B' + z
            valor3 = 'C' + z
            valor4 = 'D' + z
            valor5 = 'E' + z
            sheet[valor1] = filtro2.get('url')
            sheet[valor2] = filtro2.get('scan_date')
            sheet[valor3] = str(filtro2.get('total'))
            positivos = str(filtro2.get('positives'))
            sheet[valor4] = positivos
            positivos = int(positivos)
            if positivos > 10:
                clasificacion = 'Alta'
            elif positivos > 3:
                clasificacion = 'Media'
            else:
                clasificacion = 'Baja'
            sheet[valor5] = clasificacion
    print("Proceso terminado")
    book.save('reporte_analizador_urls.xlsx')"""


def Virus(link,apikey):
    # Aqui iniciamos creando un objeto argparse que controla el inicio de argparse
    # la descripcion y habilita la entrada del parametro -h o --help

    parser = argparse.ArgumentParser(description="Esta herramienta hace uso de la API de" +
                                        "Virus Total para analizar URLs maliciosas e informarlo" +
                                        "mediante un documento en excel. ¡Por favor ten a la mano tu" +
                                        "API Key de Virus Total!") # Aqui pones la descripcion de lo que hace el script entre la comillas

    # Aqui lo que hacemos es, mediante la funcion add_argument, iniciamos un argumento, el cual una vez parseado con el script
    # te devuelve un objeto con el link que puso el usuario
    # este argumento se puede usar -l o --link
    parser.add_argument("-l", "--link", help="Especifica el link completo.")

    parser.add_argument("-k", "--key", help="Por favor, especifica tu API Key.")

    # Aqui simplemente estamos cerrando el uso del objeto parser que creamos en la linea 66
    parser = parser.parse_args()

    # esta variable almacena la informacion que el usario proporcionó mediante el argumento -i, -k
    # los dos guiones en la linea 77 y 76, indica "el nombre completo" del parametro, y así sacas la informacion del objeto
    # ya esta varible la usas donde necesites el link

    url = parser.link
    key = parser.key

    i = 1
    Links = []
    book = Workbook()
    sheet = book.active
    sheet['A1'] = "URL"
    sheet['B1'] = "Fecha de análisis"
    sheet['C1'] = "Total de análisis"
    sheet['D1'] = "Análisis positivos"
    sheet['E1'] = "Clasificación"
    while i == 1 :
        link = input("Ingrese un link: ")
        Links.append(link)
        i = int(input("Ingrese un 1 para seguir agregando, "
                      "de lo contrario cualquier otro numero: "))
    with open('urls_sospechosas.txt', 'w') as temp_file:
        for item in Links:
            temp_file.write("%s\n" % item)
    API_KEY = "7ba043588bf8968632f5d560ad47e1438bfd36991a676ae4bbe0f179bd0fba32"
    api = PrivateApi(API_KEY)
    z = 1
    with open ("urls_sospechosas.txt", "r") as file:
        for line in file:
            response = api.get_url_report(line)
            filtro = {'results':response['results']}
            filtro2 = filtro.get('results')
            z = int(z)
            z = z + 1
            z = str(z)
            valor1 = 'A' + z
            valor2 = 'B' + z
            valor3 = 'C' + z
            valor4 = 'D' + z
            valor5 = 'E' + z
            sheet[valor1] = filtro2.get('url')
            sheet[valor2] = filtro2.get('scan_date')
            sheet[valor3] = str(filtro2.get('total'))
            positivos = str(filtro2.get('positives'))
            sheet[valor4] = positivos
            positivos = int(positivos)
            if positivos > 10:
                clasificacion = 'Alta'
            elif positivos > 3:
                clasificacion = 'Media'
            else:
                clasificacion = 'Baja'
            sheet[valor5] = clasificacion
    print("Proceso terminado")
    book.save('reporte_analizador_urls.xlsx')
