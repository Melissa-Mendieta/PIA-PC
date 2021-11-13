#!/usr/bin/env python3

import argparse
import subprocess 
import Metadatos
import Encabezados
import sublist3r
import VIRUS_01
import file_powershell
import CifradoMensajes

description = """

Suite de Seguridad:

    [1] Metadatos
    [2] Analizar encabezados
    [3] Subdominios
    [4] API
    [5] Obtener reglas de bloqueo y perfil de red
"""
parser = argparse.ArgumentParser(description, formatter_class=argparse.RawDescriptionHelpFormatter)

  # Metadatos
parser.add_argument("-m","--Metadatos", help="Escoger opción de Metadatos.", action="store_true")
parser.add_argument("-l",'--link', help="analiza imágenes desde una URL")

  # Encabezados y Subdominios
parser.add_argument("-enc","--Encabezado", help="Escoger opción de Encabezados.", action="store_true")
parser.add_argument("-subd","--Subdominio", help="Escoger opción de Subdominios.", action="store_true")
parser.add_argument("-tar","--target",help="Dominio que se investigará")
parser.add_argument("-p","--port",help="Puerto",type=int)
parser.add_argument("-P","--port2",help="Puerto para subdominios")

  # HASH
parser.add_argument("-ha","--Hash", help="Escoger opción de claves HASH.", action="store_true")
parser.add_argument("-op","--opc", type = int, help= "Escoja entre: [1] Archivos a partir de un config file\
                                                                       [2] HASH de un solo archivo")
parser.add_argument("-f", "--file", help= "Nombre o ruta del archivo de configuración o Archivo único")

  # Criptografía
parser.add_argument("-cr","--Criptografia", help="Escoger opción de Criptografía de mensajes.", action="store_true")

parser.add_argument("-mo","--modo",help=' Indica la acción a realizar: [e] Encriptar  [d] Desencriptar  [c] Crackear ')
parser.add_argument("-msj","--mensaje",help=' Mensaje para crackear, cifrar o desencriptar ')
parser.add_argument("-ps","--PyPow", help="Escoger opción de integración de Python y Powershell.", action="store_true")
parser.add_argument("-vt","--VirusTotal", help="Escoger opción de integración de API de VirusTotal.", action="store_true")
parser.add_argument("-u","--url",help=' Url a analizar ')
parser.add_argument("-ak","--apikey",help=' API Key de VirusTotal ')


params = parser.parse_args()
  
if params.Metadatos:
  Metadatos.scrapingImages(params.link)
  Metadatos.printMeta()

elif params.Encabezado:
  Encabezados.Encabezado(params.target,params.port)

elif params.Subdominio:
  sublist3r.main(params.target,10,'subdomains.txt', ports= params.port, silent=True, verbose= False, enable_bruteforce= False, engines=None)

elif params.PyPow:
  file_powershell.Ps1()

elif params.VirusTotal:
  VIRUS_01.Virus(params.url, params.apikey)

elif params.Criptografia:
  if params.modo == "e":
      CifradoMensajes.cifrado(params.mensaje)
  elif params.modo == "d":
      CifradoMensajes.decifrado(params.mensaje)
  elif params.modo == "c":
      CifradoMensajes.crackeo(params.mensaje)
  
else:
  print("Ocurrió un error al escoger la opción")




