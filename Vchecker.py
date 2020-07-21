from __future__ import with_statement
import os
import json
import requests
import wget
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def check_versions():
    try:
        with open('data.json', encoding='utf-8') as json_file:
            text = json_file.read()
            json_data = json.loads(text)

            for key in json_data.keys():
                page = requests.get(json_data[key]["url"], headers=headers)
                soup = BeautifulSoup(page.text, 'html.parser')
                version = soup.find('tbody').findChildren('td')[3].text.split(" ")[0]
                print(key + ": " + version)
    except EnvironmentError: 
        print("No existe el fichero data.json")

def check_updates(mod):
    try:
        with open('data.json', encoding='utf-8') as json_file:
            noupdates = True
            text = json_file.read()
            json_data = json.loads(text)

            for key in json_data.keys():
                page = requests.get(json_data[key]["url"], headers=headers)
                soup = BeautifulSoup(page.text, 'html.parser')
                version = soup.find('tbody').findChildren('td')[3].text.split(" ")[0]
                if(json_data[key]["Version"] != version):
                    noupdates = False
                    print(key + ": " + version)
                    if(mod == "s"):
                        json_data[key]["Version"] = version
                        try:
                            with open('data.json', 'w', encoding='utf-8') as json_file:
                                json.dump(json_data, json_file, indent=2)
                        except EnvironmentError: 
                            print("No existe el fichero data.json")
            if(noupdates == True):
                print("No se han encontrado actualizaciones")
    except EnvironmentError: 
        print("No existe el fichero data.json")

def update(mod):
    try:
        if "APKs" not in os.listdir("."):
            os.mkdir("./APKs")
    except OSError:
        print ("No se ha podido crear el directio APKs")
    try:
        with open('data.json', encoding='utf-8') as json_file:
            noupdates = True
            text = json_file.read()
            json_data = json.loads(text)

            for key in json_data.keys():
                page = requests.get(json_data[key]["url"], headers=headers)
                soup = BeautifulSoup(page.text, 'html.parser')
                version = soup.find('tbody').findChildren('td')[3].text.split(" ")[0]
                if(json_data[key]["Version"] != version):
                    noupdates = False
                    print(key + ": " + version)
                    if(mod == "s"):
                        json_data[key]["Version"] = version
                        try:
                            with open('data.json', 'w', encoding='utf-8') as json_file:
                                json.dump(json_data, json_file, indent=2)
                        except EnvironmentError: 
                            print("No existe el fichero data.json")
                    page = requests.get(json_data[key]["url"]+"download/apk", headers=headers)
                    link = None
                    while(type(link) is type(None)):
                        soup = BeautifulSoup(page.text, 'html.parser')
                        link = soup.find('a', class_="app is-small", href=True)['href']
                    print("Descargando "+key+"...")
                    wget.download(link, './APKs/'+key+'.apk')
                    print("\n")
            if(noupdates == True):
                print("No se han encontrado actualizaciones")
    except EnvironmentError: 
        print("No existe el fichero data.json")
def menu():

    os.system('cls')
    print("__      _______ _               _             ")
    print("\ \    / / ____| |             | |            ")
    print(" \ \  / / |    | |__   ___  ___| | _____ _ __ ")
    print("  \ \/ /| |    | '_ \ / _ \/ __| |/ / _ \ '__|")
    print("   \  / | |____| | | |  __/ (__|   <  __/ |   ")
    print("    \/   \_____|_| |_|\___|\___|_|\_\___|_|   ")
    print("\n\n")

    print("Selecciona una opción")
    print("\t1 - Comprobar versiones")
    print("\t2 - Comprobar actualizaciones")
    print("\t3 - Descargar actualizaciones")
    print("\t4 - Acerca de")
    print("\t0 - salir")


while True:
        # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        print("")
        print("Comprobando versiones...")
        check_versions()
        input("\n------------------------------------------------------------------------\nVersiones comprobadas, pulsa una tecla para continuar")
    elif opcionMenu == "2":
        print("")
        mod = input("¿Desea modificar el fichero JSON?(s/n)[n]") or "n"
        print("Comprobando actualizaciones...")
        check_updates(mod)
        input("\n------------------------------------------------------------------------\nActualizaciones comprobadas, pulsa una tecla para continuar")
    elif opcionMenu == "3":
        print("")
        mod = input("¿Desea modificar el fichero JSON?(s/n)[n]") or "n"
        print("Comprobando actualizaciones...")
        update(mod)
        input("\n------------------------------------------------------------------------\nActualizaciones descargadas, pulsa una tecla para continuar")
    elif opcionMenu == "4":
        print("")
        input("Código hecho por Pablo Olivas\nGithub: https://github.com/NecaX\nProyecto: https://github.com/NecaX/Vchecker")
        input("pulsa una tecla para continuar")
    elif opcionMenu == "0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
