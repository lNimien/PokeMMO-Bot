import time
from PIL import Image
import tkinter as tk
import sys
from PIL import Image, ImageTk
from pathlib import Path
import requests
import subprocess

SERVER_IP ="192.168.1.100"
SERVER_PORT = "1345"
archivo_config = 'settings.json'
SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}"
EnlaceDiscord = "https://discord.gg/xxxxxxx"
current_version = "1.2"



def check_for_update():
    global current_version
      # current version of your client
    response = requests.get(SERVER_URL +"/check_update", params={'client_version': current_version})

    if response.status_code == 200:
        data = response.json()
        
        NeedUpdate = data['update']
        print(NeedUpdate)
        if 'files' in data and NeedUpdate :  # check if there are files to download (update)
            files_to_download = data['files']
            for file_name in files_to_download:
                update_file_url = f'{SERVER_URL}/download_update/{file_name}'
                r = requests.get(update_file_url)
                with open(file_name, 'wb') as file:
                    file.write(r.content)
            
            # it opens the application again after the update
            subprocess.Popen(['PokemonMMO_bot.exe'])
            sys.exit()  # Cierra la aplicación actual
        else:
            print("La aplicación ya está actualizada.")
            return True
    else:
        print("Error al verificar actualizaciones.")
        return False








def main():
    
    print("░██████╗░█████╗░██╗░░██╗███████╗██╗░░██╗██╗░░██╗░██████╗░")
    print("██╔══██╗██╔══██╗██║░██╔╝██╔════╝██║░░██║██║░░██║██╔═══██╗")
    print("██████╔╝██║░░██║█████╔╝░█████╗░░███████║███████║██║░░░██║")
    print("██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██╔══██║██╔══██║██║░░░██║")
    print("██║░░░░░╚█████╔╝██║░░██╗███████╗██║░░██║██║░░██║╚██████╔╝")
    print("╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░")
    print("///////////////////////////////////////////////////////////")
    print("///////////////////////////////////////////////////////////")
    print("PokeMMO bot Develop By Nimien")
    print("Checking for updates")
    time.sleep(1)
    print("Checking.")
    time.sleep(1)
    print("Checking..")
    time.sleep(1)
    print("Checking...")
    time.sleep(1)
    print("Checking....")
    #comprobamos si hay alguna update
    EstaActualizado = check_for_update()
    if EstaActualizado == False:
        sys.exit(1)


if __name__ == "__main__":
    main()