import pyautogui
import pydirectinput
import time
import random
import pytesseract
import tkinter as tk
import requests
import os
import sys
import json

import threading
import datetime
#variables global

from Funciones import *
from Imagenes import *
from Traducciones import *
from Keyboard import *
from tkinter import messagebox,Canvas, Entry, Button, PhotoImage

archivo_config = 'settings.json'

permisos_premium = False
nTextosenpantalla = 0
NickNameServer = ""
PremiumServer = ""
keydateServer = ""
token = ""
nTries = 0 
nApagar = 0
TimeToleft = 0
UbicacionTesseract = ""
bNightMode = False
nTriesTentacruel = 0
nTriesLuvDisc = 0
nTriesTeselia = 0
nApagarLuvDisc = 0
nApagarTeselia = 0
nTriesMagikarp = 0
nApagarMagikarp = 0
UpKey = 0
DownKey = 0
RightKey = 0
LeftKey = 0
nNumVecesLadron = 0
IsZanabaNeeded = 0
numZanamaUsed = 0
numItemsAdquierd = 0
numPokeballsUsed = 0
numCatchesDone = 0
nNumIrCentro = 0
bIsRunningBot = False
traducted_msg = {} 
ZanamaUsed = 0
ItemsAdquired = 0
CatchesDone = 0
PokeballsUsed = 0
bUseZanama = False

ZanamaGibleSpore = 0
ZanamaGibleFalsotortazo = 0
IsParaliz = False
#################################
########### JSON DATA ###########
#################################

def load_config(nombre_archivo):
    global bNightMode, nTriesTentacruel, nTriesLuvDisc, nApagarLuvDisc, nTriesMagikarp, nApagarMagikarp, nTriesTeselia, nApagarTeselia
    global UpKey,DownKey,RightKey,LeftKey,traducted_msg
    global UbicacionTesseract
    try:
        with open(nombre_archivo, 'r') as archivo:
            config = json.load(archivo)

            #lang
            idioma_seleccionado = config.get('lang', 'es')  # get lang from map
            traducted_msg = mensajes.get(idioma_seleccionado, mensajes['en'])  # deffect eng

            bNightMode = config.get('bNightMode', False)
            nTriesTentacruel = config.get('nTriesTentacruel', 0)
            nTriesLuvDisc = config.get('nTriesLuvDisc', 0)
            nApagarLuvDisc = config.get('nApagarLuvDisc', 0)
            nTriesMagikarp = config.get('nTriesMagikarp', 0)
            nApagarMagikarp = config.get('nApagarMagikarp', 0)
            nTriesTeselia = config.get('nTriesTeselia', 0)
            nApagarTeselia = config.get('nApagarTeselia', 0)
            UpKey = config.get('UpKey', "W")
            DownKey = config.get('DownKey', "S")
            RightKey = config.get('RightKey', "D")
            LeftKey = config.get('LeftKey', "A")
            UbicacionTesseract = config.get('UbicacionTesseract', UbicacionTesseract)
            pytesseract.pytesseract.tesseract_cmd = UbicacionTesseract
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        sys.exit()
    except json.JSONDecodeError:
        messagebox.showerror("Error", "File is invalid / not a json.")
        sys.exit()
    except KeyError:
        messagebox.showerror("Error", "Missing some parameters for the file.")
        sys.exit()




#################################

# Clases

class User:
    Username = ""
    IsPremium = False
    IsLogged = False
    KeyDate = "None"



def text_to_console(widget):
    class ConsolaRedirigida:
        def __init__(self, widget):
            self.widget = widget

        def write(self, text):
            self.widget.insert(tk.END, text)
            self.widget.see(tk.END)

    consola_redirigida = ConsolaRedirigida(widget)
    sys.stdout = consola_redirigida
    sys.stderr = consola_redirigida

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



#################################
########### UTILS ############
#################################

def IrAlSiteoCazarYCurarseMagikarpsHoeen():
    global UpKey,DownKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 6)
    KeepPushedKey(DownKey,4)
    KeepPushedKey(LeftKey,.15)
    KeepPushedKey('Z', 2)

def OpenBag():
    # click bag
    global DownKey,UpKey,RightKey,LeftKey
    Send_Texto_To_Console(traducted_msg.get('abrir_bolsa'))
    time.sleep(0.1)
    KeepPushedKeyNatural(RightKey, 0.2)
    time.sleep(0.1)
    KeepPushedKeyNatural('z', 0.2)
    time.sleep(0.1)

def IrCentroPokemonLuvdiscV1():
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 6)
    KeepPushedKeyNatural(DownKey,2.5)
    KeepPushedKeyNatural(LeftKey,1.2)
    KeepPushedKeyNatural(DownKey,.5)
    KeepPushedKeyNatural('Z', 2)

def IrCentroPokemonLuvdiscV2():
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 6)
    KeepPushedKeyNatural(DownKey,2.5)
    KeepPushedKeyNatural(LeftKey,1.4)
    KeepPushedKeyNatural(DownKey,.5)
    KeepPushedKeyNatural('Z', 2)

def IrSiteoCurarseEXPHoeen():
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 6)
    KeepPushedKeyNatural(DownKey,2.5)
    KeepPushedKeyNatural("2",.1)
    KeepPushedKeyNatural(RightKey,2)
    KeepPushedKeyNatural(DownKey,.50)
    KeepPushedKeyNatural(RightKey,1)
    KeepPushedKeyNatural(DownKey,.20)
    KeepPushedKeyNatural('Z', 2)
    time.sleep(2)

def MirarSiTieneItemElPokemon():
    time.sleep(0.1)
    pydirectinput.click(1892, 425)
    time.sleep(0.2)
    TieneObjeto = verificar_texto_en_pantalla(traducted_msg.get('quitar_item_text'), 141 ,178, 45, -840)
    if TieneObjeto == True:
        time.sleep(0.2)
        pydirectinput.click(1793, 482)
        time.sleep(0.2)
        pydirectinput.click(1793, 482)
        return True
    else:
        time.sleep(0.2)
        TieneObjeto1 = verificar_texto_en_pantalla(traducted_msg.get('quitar_item_text'), 141 ,178, 45, -840)
        if TieneObjeto1 == True:
            time.sleep(0.2)
            pydirectinput.click(1793, 482)
            time.sleep(0.2)
            pydirectinput.click(1793, 482)
            return True
        else:
            time.sleep(0.5)
            pydirectinput.click(1892, 425) # clicamos en el meowth
            time.sleep(0.6)

def MirarSiMeHanSusurrado():
    time.sleep(0.1)
    bHaySusurro = verificar_texto_en_pantalla(traducted_msg.get('texto_susurros'), 416, 108, -421, 750)
    
    if bHaySusurro:
        KeepPushedKey("8")
        time.sleep(3)
    

def IrCentroPokemonBahiaAreniscaV1(): # working
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 9)
    KeepPushedKeyNatural(DownKey,2.5)
    KeepPushedKeyNatural(LeftKey,1)
    KeepPushedKeyNatural(DownKey,1.6)

def IrCentroPokemonBahiaAreniscaV2(): # working 
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 10)
    KeepPushedKeyNatural(DownKey,2.5)
    KeepPushedKeyNatural(LeftKey,1.2)
    KeepPushedKeyNatural(DownKey,0.6)
    KeepPushedKeyNatural(RightKey,2)
    KeepPushedKeyNatural(DownKey,0.3)


def IrCentroPokemonPuebloLadrillo(): # working
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 10)
    KeepPushedKeyNatural(DownKey,2.5)
    time.sleep(.3)
    KeepPushedKeyNatural("2", .2)
    KeepPushedKeyNatural(LeftKey,1.2)
    KeepPushedKeyNatural(UpKey,.4)

def IrCentroPokemonTorreDuodraco(): # working
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKey("8")
    time.sleep(3)
    KeepPushedKey('Z', 10)
    KeepPushedKeyNatural(DownKey,2.7)
    time.sleep(.3)
    KeepPushedKeyNatural("2", .2)
    KeepPushedKeyNatural(LeftKey,.4)
    KeepPushedKeyNatural(UpKey,3.7)

def UsarAntiparaliz():
    time.sleep(0.5)
    KeepPushedKey("3")
    time.sleep(0.5)
    pydirectinput.click(897, 530)
    time.sleep(0.2)
    pydirectinput.click(897, 530)
    time.sleep(0.5)
    pydirectinput.click(897, 530)
    time.sleep(0.2)
    pydirectinput.click(897, 530)

def UsarBayaZanama(posicion = 1): # working
    if posicion == 1:
        time.sleep(0.5)
        KeepPushedKey("7")
        time.sleep(0.5)
        pydirectinput.click(897, 530)
        time.sleep(0.2)
        pydirectinput.click(897, 530)
        time.sleep(0.5)
        pydirectinput.click(897, 530)
        time.sleep(0.2)
        pydirectinput.click(897, 530)
    elif posicion == 2:
        time.sleep(0.5)
        KeepPushedKey("7")
        time.sleep(0.7)
        pydirectinput.click(897, 530)
        time.sleep(0.5)
        pydirectinput.click(1122, 534)
        time.sleep(0.5)
        pydirectinput.click(1122, 534)
        
#Creamos un Mapa
versiones = {
    1: IrCentroPokemonBahiaAreniscaV1,
    2: IrCentroPokemonBahiaAreniscaV2
}

def VolverAlLagoZonaSafariKanto():
    global DownKey,UpKey,RightKey,LeftKey
    KeepPushedKeyNatural(UpKey, .2)
    KeepPushedKey('Z', 10)
    KeepPushedKeyNatural(UpKey, 1.4)
    KeepPushedKeyNatural(RightKey, 1)
    KeepPushedKeyNatural(UpKey, .6)
    KeepPushedKeyNatural('Z', 2)
    time.sleep(2)
    pescar(type = 6)


def TirarSporaGible():
    global ZanamaGibleSpore
    time.sleep(0.3)
    pydirectinput.click(416, 689)
    time.sleep(0.5)
    #Espora 2nd
    pydirectinput.click(586, 689)
    time.sleep(0.3)
    #Espora 2nd
    pydirectinput.click(586, 689)
    time.sleep(11.5)

    ZanamaGibleSpore += 1

    pydirectinput.moveTo(322, 138)
    time.sleep(0.5) # posiblemente lo baje
    SeHaDormido = verificar_texto_en_pantalla('Dormido', 55 ,29, 433, 642)
    if SeHaDormido == True:
        CapturarPokemonGible()
    else:
        TirarSporaGible()

#################################
######### LOGICA ################
#################################



###HILOS####

def IntentoDeCapturarGibleEnHilo():
    global bIsRunningBot
    bIsRunningBot = True
    time.sleep(1)
    hilo_pescar = threading.Thread(target=EncontrarGible)
    hilo_pescar.start()

def IntentoDeCapturarMeowthEnHilo():
    global bIsRunningBot
    bIsRunningBot = True
    time.sleep(1)
    hilo_pescar = threading.Thread(target=EncontrarMeowth)
    hilo_pescar.start()

def IntentoDeCapturarWhismurEnHilo():
    global bIsRunningBot
    bIsRunningBot = True
    time.sleep(1)
    hilo_pescar = threading.Thread(target=EncontrarWhismur)
    hilo_pescar.start()

def IntentoDeLadronAMeowthEnHilo():
    global bIsRunningBot
    bIsRunningBot = True
    time.sleep(1)
    hilo_pescar = threading.Thread(target=LadronMeowthUsandoBayaZanama)
    hilo_pescar.start()

def IntentoDeDulceAromaEnHilo():
    global bIsRunningBot
    bIsRunningBot = True
    time.sleep(1)
    hilo_pescar = threading.Thread(target=UsarDulceAromaShinnyMienfoo)
    hilo_pescar.start()

def IntentoDeMatarTentacruelEnHilo():
    global bIsRunningBot
    bIsRunningBot = True
    time.sleep(1)
    hilo_pescar = threading.Thread(target=MatarTentacruelsHoeenEXPAutomatico)
    hilo_pescar.start()

def IntentoDePescarEnHilo(type=0):
    Send_Texto_To_Console(traducted_msg.get('texto_comenzar_pescar'))  
    global bIsRunningBot
    bIsRunningBot = True
    hilo_pescar = threading.Thread(target=pescar, args=(type,))
    hilo_pescar.start()


###CAPTURAR#### pydirectinput.moveTo(400, 136)

def CapturarPokemonGible():
    global ZanamaGibleSpore, ZanamaGibleFalsotortazo
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    OpenBag()
    KeepPushedKey('Z', 1)
    time.sleep(14.5)
    
    EstaCapturado = verificar_texto_en_pantalla('Gible', 1351 ,85, 380)
    if EstaCapturado == True:
        Send_Texto_To_Console(traducted_msg.get('magikarp_no_capturado'))
        numPokeballsUsed += 1
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")
        pydirectinput.moveTo(322, 138)
        time.sleep(0.5) # posiblemente lo baje
        SeHaDormido = verificar_texto_en_pantalla('Dormido', 55 ,29, 433, 642)
        if SeHaDormido == True:
            CapturarPokemonGible()
        else:
            TirarSporaGible()
    else:
        Send_Texto_To_Console(traducted_msg.get('magikarp_capturado'))
        numCatchesDone += 1
        numPokeballsUsed += 1
        canvasbot.itemconfig(CatchesDone, text=f"Catches: {numCatchesDone}")
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")
        time.sleep(0.5)
        PushKey('esc')

        time.sleep(1)
        MirarSiMeHanSusurrado()    
        EncontrarGible()

def CapturarPokemonMeowth():
    ## Comprobamos si esta el usuario con la sesion activa
    global IsZanabaNeeded
    OpenBag()
    KeepPushedKey('Z', 1)
    time.sleep(13)
    
    EstaCapturado = verificar_texto_en_pantalla('Meowth', 1351 ,85, 380)
    if EstaCapturado == True:
        Send_Texto_To_Console(traducted_msg.get('magikarp_no_capturado'))
        CapturarPokemonMeowth()
    else:
        Send_Texto_To_Console(traducted_msg.get('magikarp_capturado'))
        time.sleep(0.3)
        PushKey('esc')
        IsZanabaNeeded += 1
        if IsZanabaNeeded > 9:
            IsZanabaNeeded = 0
            UsarBayaZanama()

        time.sleep(1)
        MirarSiMeHanSusurrado()    
        EncontrarMeowth()

def CapturarPokemonWhismur():
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    OpenBag()
    KeepPushedKey('Z', 1)
    time.sleep(14)
    
    EstaCapturado = verificar_texto_en_pantalla('Whismur', 1351 ,85, 380)
    if EstaCapturado == True:
        Send_Texto_To_Console(traducted_msg.get('magikarp_no_capturado'))
        numPokeballsUsed += 1
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")
        CapturarPokemonWhismur()
    else:
        Send_Texto_To_Console(traducted_msg.get('magikarp_capturado'))
        numCatchesDone += 1
        numPokeballsUsed += 1
        canvasbot.itemconfig(CatchesDone, text=f"Catches: {numCatchesDone}")
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")

        time.sleep(0.3)
        PushKey('esc')
        IsZanabaNeeded += 1
        if IsZanabaNeeded > 9:
            IsZanabaNeeded = 0
            UsarBayaZanama()
            numZanamaUsed += 1
            canvasbot.itemconfig(ZanamaUsed, text=f"Zanama: {numZanamaUsed} ")

        time.sleep(1)
        MirarSiMeHanSusurrado()    
        EncontrarWhismur()

def CapturarPokemonMagikarp():
    global nTries,nApagar,nTriesMagikarp,bNightMode
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    OpenBag()
    KeepPushedKey('Z', 1)
    time.sleep(14.5)
    
    EstaCapturado = verificar_texto_en_pantalla('Magikarp', 1351 ,85, 380)
    if EstaCapturado == True:
        Send_Texto_To_Console(traducted_msg.get('magikarp_no_capturado'))
        numPokeballsUsed += 1
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")
        CapturarPokemonMagikarp()
    else:
        Send_Texto_To_Console(traducted_msg.get('magikarp_capturado'))
        numCatchesDone += 1
        numPokeballsUsed += 1
        canvasbot.itemconfig(CatchesDone, text=f"Catches: {numCatchesDone}")
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")
        time.sleep(0.3)
        PushKey('esc')
        nTries += 1

        if nTries > nTriesMagikarp:
            nTries = 0
            IrAlSiteoCazarYCurarseMagikarpsHoeen()

        nApagar+= 1
        
        if bNightMode == True:
            if nApagar > nApagarMagikarp:
                os.system("shutdown /s /t 1") 

        
        time.sleep(1)
        MirarSiMeHanSusurrado()    
        pescar(type = 1)


bSafariBalls = 0
def CapturarPokemonMagikarpZonaSafari():
    global nTries,nApagar,nTriesMagikarp,bNightMode,bSafariBalls
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    #Primer Intento de captura
    KeepPushedKeyNatural('Z', 0.1)
    time.sleep(0.3)
    # Falsotortazo en la 1ra posición
    KeepPushedKeyNatural('Z', 0.1)
    time.sleep(0.3)
    # Falsotortazo en la 1ra posición
    KeepPushedKeyNatural('Z', 0.1)
    time.sleep(0.3)
    # Falsotortazo en la 1ra posición
    KeepPushedKeyNatural('Z', 0.1)
    bSafariBalls += 1
    time.sleep(6.1)
    if bSafariBalls > 29:
        VolverAlLagoZonaSafariKanto()
        return
    PokemonVivo = verificar_texto_en_pantalla('Nv', 167 ,26, 405, 550)
    if PokemonVivo == True:
        numPokeballsUsed += 1
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")
        CapturarPokemonMagikarpZonaSafari()
    else:
        canvasbot.itemconfig(CatchesDone, text=f"Catches: {numCatchesDone}")
        canvasbot.itemconfig(PokeballsUsed, text=f"Pokeballs: {numPokeballsUsed} ")
        time.sleep(0.3)
        PushKey('esc')
        pescar(type = 6)


###ENCONTRAR

def EncontrarMeowth():
    global DownKey,UpKey,RightKey,LeftKey
    while bIsRunningBot:
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        time.sleep(4.2)
        HaEntradoEnCombate = verificar_texto_en_pantalla('Nv', 167 ,26, 405, 550,True)
        if HaEntradoEnCombate == True:
            Send_Texto_To_Console("Hay Combate")
            time.sleep(5)
            EsUnMeowth = verificar_texto_en_pantalla('Meowth', 167 ,26, 405, 550)
            if EsUnMeowth == True:
                Send_Texto_To_Console("Es un Meowth")
                # Botón de ataque
                pydirectinput.click(416, 689)
                time.sleep(0.5)
                # Falsotortazo en la 1ra posición
                pydirectinput.click(416, 689)
                time.sleep(0.3)
                # Falsotortazo en la 1ra posición
                pydirectinput.click(416, 689)
                # Esperamos a que acaba la transicion
                time.sleep(8.5)
                pydirectinput.moveTo(400, 136)
                time.sleep(1)
                HayQueAtacarDeNuevo = verificar_texto_en_pantalla('100', 36 ,29, 429, 522,True)
                if HayQueAtacarDeNuevo == True:
                    Send_Texto_To_Console("Atacamos de nuevo")
                    # Botón de ataque
                    pydirectinput.click(416, 689)
                    time.sleep(0.5)
                    # Falsotortazo en la 1ra posición
                    pydirectinput.click(416, 689)
                    time.sleep(0.3)
                    # Falsotortazo en la 1ra posición
                    pydirectinput.click(416, 689)
                    # Esperamos a que acaba la transicion
                    time.sleep(8.5)
                    CapturarPokemonMeowth()
                    continue
                else:
                    Send_Texto_To_Console("Capturamos")
                    time.sleep(3)
                    CapturarPokemonMeowth()
                    continue
            else:
                Send_Texto_To_Console("Escapamos")
                pydirectinput.click(631, 752)
                time.sleep(0.3)
                pydirectinput.click(631, 752)
                time.sleep(0.4)
                pydirectinput.click(631, 752)
                continue
        else:
            Send_Texto_To_Console("Seguimos Caminando")
            pydirectinput.click(631, 752)
            time.sleep(0.3)
            pydirectinput.click(631, 752)
            time.sleep(0.4)
            pydirectinput.click(631, 752)
            continue

def EncontrarWhismur():
    global DownKey,UpKey,RightKey,LeftKey
    while bIsRunningBot:
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.4)
        time.sleep(4.2)
        HaEntradoEnCombate = verificar_texto_en_pantalla('Nv', 167 ,26, 405, 550,True)
        if HaEntradoEnCombate == True:
            Send_Texto_To_Console("Hay Combate")
            time.sleep(5)
            # Botón de ataque
            pydirectinput.click(416, 689)
            time.sleep(0.5)
            # Falsotortazo en la 1ra posición
            pydirectinput.click(416, 689)
            time.sleep(0.3)
            # Falsotortazo en la 1ra posición
            pydirectinput.click(416, 689)
            # Esperamos a que acaba la transicion
            time.sleep(7.5)
            CapturarPokemonWhismur()
        else:
            Send_Texto_To_Console("Seguimos Caminando")
            continue

def EncontrarGible():
    global DownKey,UpKey,RightKey,LeftKey,ZanamaGibleSpore,ZanamaGibleFalsotortazo
    global ZanamaGibleSpore, ZanamaGibleFalsotortazo, IsParaliz

    if ZanamaGibleFalsotortazo > 9:
        UsarBayaZanama(position = 1)
    if ZanamaGibleSpore > 9:
        UsarBayaZanama(posicion = 2)

    while bIsRunningBot:
        if IsParaliz == True:
            IsParaliz = False
            UsarAntiparaliz()

        KeepPushedKeyNatural(LeftKey, 0.8)
        KeepPushedKeyNatural(RightKey, 0.6)
        KeepPushedKeyNatural(LeftKey, 0.6)
        KeepPushedKeyNatural(RightKey, 0.8)
        KeepPushedKeyNatural(LeftKey, 0.4)
        KeepPushedKeyNatural(RightKey, 0.2)
        time.sleep(4.2)
        HaEntradoEnCombate = verificar_texto_en_pantalla('Nv', 167 ,26, 405, 550,True)
        if HaEntradoEnCombate == True:
            Send_Texto_To_Console("Hay Combate")
            time.sleep(5)
            EsUnGible = verificar_texto_en_pantalla('Gible', 167 ,26, 405, 550)
            if EsUnGible == True:
                Send_Texto_To_Console("Es un Gible")
                IsParaliz = True
                # Botón de ataque
                pydirectinput.click(416, 689)
                time.sleep(0.5)
                # Falsotortazo en la 1ra posición
                pydirectinput.click(416, 689)
                time.sleep(0.3)
                # Falsotortazo en la 1ra posición
                pydirectinput.click(416, 689)
                # Esperamos a que acaba la transicion
                time.sleep(12.5)

                ZanamaGibleFalsotortazo += 1

                time.sleep(0.3)
                pydirectinput.click(416, 689)
                time.sleep(0.5)
                #Espora 2nd
                pydirectinput.click(586, 689)
                time.sleep(0.5)
                #Espora 2nd
                pydirectinput.click(586, 689)
                time.sleep(13)

                ZanamaGibleSpore += 1

                pydirectinput.moveTo(322, 138)
                time.sleep(0.5) # posiblemente lo baje
                SeHaDormido = verificar_texto_en_pantalla('Dormido', 55 ,29, 433, 642)
                if SeHaDormido == True:
                    CapturarPokemonGible()
                    continue
                else:
                    TirarSporaGible()
            else:
                Send_Texto_To_Console("Escapamos")
                pydirectinput.click(631, 752)
                time.sleep(0.3)
                pydirectinput.click(631, 752)
                time.sleep(0.4)
                pydirectinput.click(631, 752)
                continue
        else:
            Send_Texto_To_Console("Seguimos Caminando")
            pydirectinput.click(631, 752)
            time.sleep(0.3)
            pydirectinput.click(631, 752)
            time.sleep(0.4)
            pydirectinput.click(631, 752)
            continue


### LADRON / DIA DE PAGO / CACHEO

def LadronMeowthUsandoBayaZanama():
    while bIsRunningBot:
        time.sleep(1)
        PushKey('9')
        KeepPushedKey('Z', 10.5)
        resultado = verificar_texto_en_pantalla('Meowth',925,149, 390)
        if resultado == True: #Es un meowth
            Send_Texto_To_Console(traducted_msg.get('info_meowth'))
            time.sleep(0.3)
            TieneObjetoCacheo = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 470, True)
            time.sleep(0.3)
            TieneObjetoNombrePokemon = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 520, True)
            time.sleep(0.1)
            TieneObjetoNombrePokemon2 = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 520, True)
            time.sleep(0.2)
            TieneObjetoNombrePokemon3 = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 520, True)
            if TieneObjetoCacheo == True or TieneObjetoNombrePokemon == True or TieneObjetoNombrePokemon2 == True or TieneObjetoNombrePokemon3 == True:
                time.sleep(2)
                UtilizarLadronMultiplesVeces()
                time.sleep(2)
                MirarSiTieneItemElPokemon()
                continue
            else:
                time.sleep(2)
                pydirectinput.click(631, 752)
                time.sleep(0.3)
                pydirectinput.click(631, 752)
                time.sleep(0.4)
                pydirectinput.click(631, 752)
                time.sleep(2)
                continue
        else:
            time.sleep(2.5)
            pydirectinput.click(631, 752)
            time.sleep(0.3)
            pydirectinput.click(631, 752)
            time.sleep(0.4)
            pydirectinput.click(631, 752)
            time.sleep(2)
            continue

def UtilizarLadronMultiplesVeces():
    global nNumVecesLadron
    while bIsRunningBot:
        pydirectinput.click(416, 689)
        time.sleep(0.5)
        # Botón de ataque
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        # Falsotortazo en la 1ra posición
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        # Falsotortazo en la 1ra posición
        pydirectinput.click(416, 689)
        if nNumVecesLadron == 0:
            time.sleep(28)
        elif nNumVecesLadron == 1:
            time.sleep(25)
        elif nNumVecesLadron == 2:
            time.sleep(23)
        elif nNumVecesLadron == 3:
            time.sleep(20)
        elif nNumVecesLadron == 4:
            time.sleep(17)
        else:
            time.sleep(14)

        TieneItem = MirarSiTieneItemElPokemon()
        if TieneItem == True:
            time.sleep(1.5)
            Send_Texto_To_Console(traducted_msg.get('info_text_robar'))
            pydirectinput.click(631, 752)
            time.sleep(0.3)
            pydirectinput.click(631, 752)
            time.sleep(0.4)
            pydirectinput.click(631, 752)
            nNumVecesLadron = 0
            return
        else:
            nNumVecesLadron+= 1
            continue

def CacheoLuvdisc():
    global nApagar,nTries
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    Send_Texto_To_Console(traducted_msg.get('inicio_de_cacheo_luvdisc'))
    EsUnLuvdisc = verificar_texto_en_pantalla('Luvdise', 167 ,26, 405, 550)
    if EsUnLuvdisc == True:
        Send_Texto_To_Console(traducted_msg.get('luvdisc_encontrado'))
        time.sleep(0.3)
        TieneObjetoCacheo = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 470, True)
        time.sleep(0.3)
        TieneObjetoNombrePokemon = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 520, True)
        time.sleep(0.1)
        TieneObjetoNombrePokemon2 = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 520, True)
        time.sleep(0.2)
        TieneObjetoNombrePokemon3 = verificar_texto_en_pantalla(traducted_msg.get('texto_cacheo'), 250 ,60, -90, 520, True)
        if TieneObjetoCacheo == True or TieneObjetoNombrePokemon == True or TieneObjetoNombrePokemon2 == True or TieneObjetoNombrePokemon3 == True:
            # Botón de ataque
            pydirectinput.click(416, 689)
            time.sleep(0.3)
            # Ladron en la 2ra posición
            pydirectinput.click(586, 689)
            time.sleep(0.3)
            # Ladron en la 2ra posición
            pydirectinput.click(586, 689)
            time.sleep(11)
            MirarSiTieneItemElPokemon()
            numItemsAdquierd += 1
            canvasbot.itemconfig(ItemsAdquired, text=f"Items: {numCatchesDone}") 
            nTries+= 1
            if nTries > nTriesLuvDisc:
                nTries = 0
                time.sleep(1)
                probabilidad = random.random() 
                if probabilidad < 0.5:
                    IrCentroPokemonLuvdiscV1()
                else:
                    IrCentroPokemonLuvdiscV2()    
        else:
            Send_Texto_To_Console(traducted_msg.get('texto_escapar'))
            time.sleep(0.2)
            pydirectinput.click(631, 752)
            time.sleep(0.2)
            pydirectinput.click(631, 752)
            time.sleep(5)
    else:
        Send_Texto_To_Console(traducted_msg.get('texto_escapar'))
        time.sleep(0.2)
        pydirectinput.click(631, 752)
        time.sleep(0.2)
        pydirectinput.click(631, 752)
        time.sleep(5)
            
            
    

    if bNightMode == True:
        if nApagar > nApagarLuvDisc:
            os.system("shutdown /s /t 1") 

    nApagar+= 1
    time.sleep(0.5)
    MirarSiMeHanSusurrado()   

def LadronLuvdiscEnHoeen():
    global nApagar,nTries
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    Send_Texto_To_Console(traducted_msg.get('inicio_de_ladron_luvdisc'))
    EsUnLuvdisc = verificar_texto_en_pantalla('Luvdise', 167 ,26, 405, 550)
    if EsUnLuvdisc == True:
        Send_Texto_To_Console(traducted_msg.get('luvdisc_encontrado'))
        # Botón de ataque
        time.sleep(0.2)
        pydirectinput.click(416, 689)
        time.sleep(0.5)
        # Ladron en la 2ra posición
        pydirectinput.click(586, 689)
        time.sleep(0.3)
        # Ladron en la 2ra posición
        pydirectinput.click(586, 689)
        time.sleep(9)
    else:
        EsUnCorsola = verificar_texto_en_pantalla('Corsola', 167 ,26, 405, 550)
        if EsUnCorsola == True:
            Send_Texto_To_Console(traducted_msg.get('corsola_encontrado'))     
            time.sleep(0.2)
            pydirectinput.click(631, 752)
            time.sleep(0.2)
            pydirectinput.click(631, 752)
            time.sleep(5)
            Send_Texto_To_Console("Escapamos")
        else:
            Send_Texto_To_Console(traducted_msg.get('texto_atacamos'))
            # Botón de ataque
            pydirectinput.click(416, 689)
            time.sleep(0.3)
            # Dia de Pago en la 1ra posición
            pydirectinput.click(416, 689)
            time.sleep(0.3)
            # Dia de Pago en la 1ra posición
            pydirectinput.click(416, 689)
            time.sleep(9)

    nTries+= 1

    if nTries > nTriesLuvDisc:
        nTries = 0
        time.sleep(1)
        probabilidad = random.random() 
        if probabilidad < 0.5:
            IrCentroPokemonLuvdiscV1()
        else:
            IrCentroPokemonLuvdiscV2()

    nApagar+= 1

    if bNightMode == True:
        if nApagar > nApagarLuvDisc:
            os.system("shutdown /s /t 1") 

    
    
    time.sleep(1.5)
    resultado = MirarSiTieneItemElPokemon()
    if resultado == True:
        numItemsAdquierd += 1
        canvasbot.itemconfig(ItemsAdquired, text=f"Items: {numCatchesDone}") 

    time.sleep(0.5)
    MirarSiMeHanSusurrado() 

def DiaDePago_Ladron_Bahia_Arenisca():
    global nApagar,nTries,bUseZanama,nTriesTeselia
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    Send_Texto_To_Console(traducted_msg.get('inicio_de_ladron_cacheo_luvdisc'))
    time.sleep(0.2)
    EsUnLuvdisc = verificar_texto_en_pantalla('Luvdise', 167 ,26, 405, 550)
    time.sleep(0.3)
    EsUnShellder = verificar_texto_en_pantalla('Shellder', 167 ,26, 405, 550)
    if EsUnLuvdisc == True or EsUnShellder == True:
        if EsUnLuvdisc == True:
            Send_Texto_To_Console(traducted_msg.get('luvdisc_encontrado'))
        else:
            Send_Texto_To_Console(traducted_msg.get('Shellder_encontrado'))
            
        time.sleep(0.3)
        pydirectinput.click(416, 689)
        time.sleep(0.5)
        #Ladron 2nd
        pydirectinput.click(586, 689)
        time.sleep(0.3)
        #Ladron 2nd
        pydirectinput.click(586, 689)
        time.sleep(10)
        pydirectinput.moveTo(400, 136)
        time.sleep(1)
        HayQueAtacarDeNuevo = verificar_texto_en_pantalla('100', 36 ,29, 429, 522,True)
        if HayQueAtacarDeNuevo == True:
            #Send_Texto_To_Console("Atacamos de nuevo")
            # Botón de ataque
            pydirectinput.click(416, 689)
            time.sleep(0.5)
            #Ladron 2nd
            pydirectinput.click(586, 689)
            time.sleep(0.3)
            #Ladron 2nd
            pydirectinput.click(586, 689)
            time.sleep(10)
                
        PokemonVivo = verificar_texto_en_pantalla('Nv', 167 ,26, 405, 550)
        if PokemonVivo == True:
            #Send_Texto_To_Console(traducted_msg.get('texto_atacamos_otravez'))
            time.sleep(0.3)
            pydirectinput.click(416, 689)
            time.sleep(0.5)
            pydirectinput.click(416, 689)
            time.sleep(0.3)
            # Dia de Pago
            pydirectinput.click(416, 689)
            time.sleep(10)
    else:
        time.sleep(0.3)
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        # Dia de Pago
        pydirectinput.click(416, 689)
        time.sleep(10)
            

    if nTries > nTriesTeselia:
        nTries = 0
        time.sleep(2)
        IrCentroPokemonBahiaAreniscaV1()
    """elif nTries > 8 and bUseZanama:
        nTries = 0
        time.sleep(2)
        UsarBayaZanama()
        numZanamaUsed += 1
        canvasbot.itemconfig(ZanamaUsed, text=f"Zanama: {numZanamaUsed} ")"""
        
    if bNightMode == True:
        if nApagar > nApagarTeselia:
            os.system("shutdown /s /t 1") 
        mensaje1 = traducted_msg.get('texto_apagar_pc').format(TimeToTurnOffPC = nApagarTeselia - nApagar)
        Send_Texto_To_Console(mensaje1)   

    nApagar+= 1
    nTries+= 1
    time.sleep(1)
    resultado = MirarSiTieneItemElPokemon()
    if resultado == True:
        numItemsAdquierd += 1
        canvasbot.itemconfig(ItemsAdquired, text=f"Items: {numItemsAdquierd}")

    time.sleep(0.5)
    #MirarSiMeHanSusurrado()

### DULCE AROMA / SHINNY / EVS / EXP

def UsarDulceAromaShinnyMienfoo():
    global nNumIrCentro
    while bIsRunningBot:
        time.sleep(2)
        PushKey('9')
        KeepPushedKey('Z', 11.5)
        resultado = verificar_texto_en_pantalla('Variocolor',925,149, 390,0,True)
        if resultado == True: #Es un shinni
            sys.exit()
        else:
            time.sleep(1)
            pydirectinput.click(631, 752)
            time.sleep(0.3)
            pydirectinput.click(631, 752)
            time.sleep(0.4)
            pydirectinput.click(631, 752)
            time.sleep(2)

            nNumIrCentro += 1

            if nNumIrCentro > 4:
                IrCentroPokemonTorreDuodraco()
                nNumIrCentro = 0
                

def MatarRapidashTeselia():
    global nTries
    time.sleep(1)
    PushKey('9')
    KeepPushedKey('Z', 11.4)
    # Botón de ataque
    KeepPushedKeyNatural("Z",0.2)
    KeepPushedKeyNatural("Z",0.2)
    time.sleep(0.3)
    # Falsotortazo en la 1ra posición
    KeepPushedKeyNatural("Z",0.2)
    KeepPushedKeyNatural("Z",0.2)
    time.sleep(0.3)
    # Falsotortazo en la 1ra posición
    KeepPushedKeyNatural("Z",0.2)
    KeepPushedKeyNatural("Z",0.2)
    time.sleep(11)
    nTries += 1

    if nTries > nTriesTentacruel:
        nTries = 0
        time.sleep(2)
        IrCentroPokemonPuebloLadrillo()

    time.sleep(1)
    MatarRapidashTeselia()

def MatarTentacruelsHoeenEXPAutomatico():
    global bIsRunningBot,nTries
    while bIsRunningBot:
        time.sleep(1)
        PushKey('9')
        KeepPushedKey('Z', 12)
        # Botón de ataque
        pydirectinput.click(416, 689)
        time.sleep(0.5)
        # Falsotortazo en la 1ra posición
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        # Falsotortazo en la 1ra posición
        pydirectinput.click(416, 689)
        time.sleep(13)
        nTries += 1

        if nTries > nTriesTentacruel:
            nTries = 0
            time.sleep(2)
            IrSiteoCurarseEXPHoeen()

        time.sleep(1)

def DulceAromaAutomatico():
    global bIsRunningBot,nTries
    while bIsRunningBot:
        PushKey('9')
        KeepPushedKeyNatural('Z', 0.5)
        time.sleep(14)
        # Botón de ataque
        KeepPushedKeyNatural('Z', 0.1)
        time.sleep(0.3)
        # Falsotortazo en la 1ra posición
        KeepPushedKeyNatural('Z', 0.1)
        time.sleep(0.3)
        # Falsotortazo en la 1ra posición
        KeepPushedKeyNatural('Z', 0.1)
        time.sleep(0.3)
        # Falsotortazo en la 1ra posición
        KeepPushedKeyNatural('Z', 0.1)
        time.sleep(8.1)


### PRINCIPAL

def pescar(type = 0):
    global bIsRunningBot
    while bIsRunningBot:
        time.sleep(0.2)
        PushKey('1')
        time.sleep(2.7)
        resultado = verificar_texto_en_pantalla(traducted_msg.get('texto_a_picado_un_pkm'),925,149, 390)
        if resultado == True:
            KeepPushedKey('Z', 0.1)
            time.sleep(9.2)
            CazarElPescado(type)
        else:
            KeepPushedKey('Z', 0.1)
            Send_Texto_To_Console(traducted_msg.get('texto_no_ha_picado_pkm'))

def CazarElPescado(type = 0):
    global nApagar,nTries
    global IsZanabaNeeded,ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed,numZanamaUsed,numItemsAdquierd,numPokeballsUsed,numCatchesDone
    if type == 1: # capturar magikarps
        Send_Texto_To_Console(traducted_msg.get('inicio_de_pesca_magikarp'))
        time.sleep(0.5)
        pydirectinput.click(416, 689)
        time.sleep(0.6)
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        # Dia de Pago
        pydirectinput.click(416, 689)
        time.sleep(0.2)
        pydirectinput.click(416, 689)
        time.sleep(8.2)
        CapturarPokemonMagikarp()
    elif type == 2: # ladron a luvdisc
        LadronLuvdiscEnHoeen()
        pescar(type = 2) 
    elif type == 3: # cacheo a luvdisc
        CacheoLuvdisc()
        pescar(type = 3) 
    elif type == 4: # Teselia Bahia Arenisca
        DiaDePago_Ladron_Bahia_Arenisca()
        pescar(type = 4) 
    elif type == 5: # Teselia Torreduodraco
        Send_Texto_To_Console(traducted_msg.get('inicio_de_dia_de_pago_teselia'))
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        pydirectinput.click(416, 689)
        time.sleep(0.3)
        # Dia de Pago
        pydirectinput.click(416, 689)
        time.sleep(8.8)
        PokemonVivo1 = verificar_texto_en_pantalla('Basculin', 1351 ,85, 380)
        PokemonVivo2 = verificar_texto_en_pantalla('Dratini', 1351 ,85, 380)
        PokemonVivo3 = verificar_texto_en_pantalla('Dragonair', 1351 ,85, 380)
        if PokemonVivo1 == True or PokemonVivo2 == True or PokemonVivo3 == True:
            Send_Texto_To_Console(traducted_msg.get('texto_atacamos_otravez'))
            pydirectinput.click(416, 689)
            time.sleep(0.3)
            pydirectinput.click(416, 689)
            time.sleep(0.3)
            # Dia de Pago
            pydirectinput.click(416, 689)
            time.sleep(8.8)
            nTries+= 1
            
        if nTries > 8:
            nTries = 0
            time.sleep(2)
            UsarBayaZanama()
        
        mensaje = traducted_msg.get('texto_usos_de_baya_zanama').format(TimeToleft = 8 - nTries)
        Send_Texto_To_Console(mensaje)

        if bNightMode == True:
            if nApagar > nApagarTeselia:
                os.system("shutdown /s /t 1")
            nApagar+= 1 
            mensaje1 = traducted_msg.get('texto_apagar_pc').format(TimeToTurnOffPC = nApagarTeselia - nApagar)
            Send_Texto_To_Console(mensaje1)   
        
        
        nTries+= 1
        MirarSiMeHanSusurrado()
        pescar(type = 5) 
    elif type == 6:
        CapturarPokemonMagikarpZonaSafari()
    else:
        main()


#################################
########### FUNCIONES ###########
#################################

def cerrar_ventana_login(event=None):
    sys.exit() 

def cerrar_ventana_bot(event=None):
    global bIsRunningBot
    
    if bIsRunningBot == True:
        Send_Texto_To_Console(traducted_msg.get('texto_cerar_programa_bot_on'))
    else:
        handle_exit(username=NickNameServer, token=token)
        sys.exit() 


    global x, y
    x = event.x_root - window.winfo_x()
    y = event.y_root - window.winfo_y()

def cambiar_valor():
    global bUseZanama
    bUseZanama = variable_global.get()
    if bUseZanama == True:
        checkbox.config(bg='#0c1c2c',fg="Green")  
    else:
        checkbox.config(bg='#0c1c2c',fg="Red")  
    print(bUseZanama)
    
#################################

def mostrar_info(event):
    Send_Texto_To_Console("Este botón activa/desactiva la función Zanama")


def PararBot():
    global bIsRunningBot
    bIsRunningBot = False
    Send_Texto_To_Console(traducted_msg.get('texto_parar_bot'))

def mostrar_combate():
    boton_torre_duodraco_teselia.place(x=250, y=170)
    boton_pueblo_arenisca_teselia.place(x=250, y=200)

    #ocultamos los otros
    boton_exp_tentacruel_hoeen.place_forget()
    boton_terremoto_automatico.place_forget()
    boton_farmeo_cacheo_luvdisc.place_forget()
    boton_farmeo_MonAmuleto_Kanto.place_forget()

    #ocultamos los otros
    boton_capturar_magikarps_hoeen.place_forget()
    boton_capturar_meowths_kanto.place_forget()
    boton_capturar_gible_shinno.place_forget()
    boton_capturar_whismur_hoeen.place_forget()
    boton_capturar_shinny_mienshao.place_forget()
    boton_farmeo_kanto_zona_safari_magikarp.place_forget()

    global NickNameServer,token

def mostrar_farmeo():
    boton_exp_tentacruel_hoeen.place(x=250, y=170)
    boton_terremoto_automatico.place(x=250, y=200)
    boton_farmeo_cacheo_luvdisc.place(x=250, y=230)
    boton_farmeo_MonAmuleto_Kanto.place(x=250,y=260)

    #ocultamos los otros
    boton_torre_duodraco_teselia.place_forget()
    boton_pueblo_arenisca_teselia.place_forget()
    #ocultamos los otros
    boton_capturar_magikarps_hoeen.place_forget()
    boton_capturar_meowths_kanto.place_forget()
    boton_capturar_gible_shinno.place_forget()
    boton_capturar_whismur_hoeen.place_forget()
    boton_capturar_shinny_mienshao.place_forget()
    boton_farmeo_kanto_zona_safari_magikarp.place_forget()

def mostrar_cazar():
    boton_capturar_magikarps_hoeen.place(x=250, y=170)
    boton_capturar_shinny_mienshao.place(x=250, y=200)
    boton_capturar_meowths_kanto.place(x=250, y=230)
    boton_capturar_whismur_hoeen.place(x=250, y=260)
    boton_farmeo_kanto_zona_safari_magikarp.place(x=250, y=290)
    boton_capturar_gible_shinno.place(x=250,y=320)

    #ocultamos los otros
    boton_exp_tentacruel_hoeen.place_forget()
    boton_terremoto_automatico.place_forget()
    boton_farmeo_cacheo_luvdisc.place_forget()
    boton_farmeo_MonAmuleto_Kanto.place_forget()

    #ocultamos los otros
    boton_torre_duodraco_teselia.place_forget()
    boton_pueblo_arenisca_teselia.place_forget()
    global NickNameServer,token

def AbrirInterfazBot():

    global keydateServer,NickNameServer,PremiumServer
    # Crear la ventana
    global windowbot
    windowbot = tk.Tk()
    windowbot.title("5Lm2Xeh2Sa")


    window_width = 842
    window_height = 606
    windowbot.configure(bg = "#FFFFFF")

    screen_width = windowbot.winfo_screenwidth()
    screen_height = windowbot.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    windowbot.geometry(f"{window_width}x{window_height}+{x}+{y}")


    windowbot.bind("<ButtonPress-1>", lambda event: on_drag_start_windowbot(windowbot,event))
    windowbot.bind("<B1-Motion>",lambda event: move_windowbot(windowbot,event))
    windowbot.overrideredirect(True)
    windowbot.attributes("-topmost", True)
    #creamos el canvas
    global canvasbot
    canvasbot = Canvas(windowbot,bg = "#FFFFFF",height = 606,width = 842,bd = 0,highlightthickness = 0,relief = "ridge")
    canvasbot.place(x = 0, y = 0)

    #rectangulos con color
    canvasbot.create_rectangle(0.0,0.0,167.0,606.0,fill="#0C1C2C",outline="")
    canvasbot.create_rectangle(166.0,0.0,842.0,104.0,fill="#101F30",outline="")

    

    #Logo
    path = resource_path("assets/frame1/image_1.png")
    image_image_1 = PhotoImage(file=path)
    image_1 = canvasbot.create_image(83.0,55.0,image=image_image_1)

    #rectangulo texto
    canvasbot.create_rectangle(187.0,72.0,312.0,93.0,fill="#0D454D",outline="")

    canvasbot.create_rectangle(334.0,72.0,459.0,93.0,fill="#0D454D",outline="")

    canvasbot.create_text(
    192.0,
    52.0,
    anchor="nw",
    text=traducted_msg.get('texto_username'),
    fill="#FFFFFF",
    font=("IrishGrover Regular", 16 * -1)
    )

    canvasbot.create_text(
        29.0,
        586.0,
        anchor="nw",
        text="Version : " + current_version,
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    canvasbot.create_text(
        340.0,
        54.0,
        anchor="nw",
        text=traducted_msg.get('texto_estado'),
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    canvasbot.create_rectangle(
        479.0,
        72.0,
        604.0,
        93.0,
        fill="#0D454D",
        outline="")

    canvasbot.create_text(
        485.0,
        54.0,
        anchor="nw",
        text="Key\n",
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    canvasbot.create_text(
        195.0,
        74.0,
        anchor="nw",
        text=NickNameServer,
        fill="#FFFFFF",
        font=("IrishGrover Regular", 12 * -1)
    )

    canvasbot.create_text(
        340.0,
        75.0,
        anchor="nw",
        text=PremiumServer,
        fill="#FFFFFF",
        font=("IrishGrover Regular", 12 * -1)
    )

    canvasbot.create_text(
        483.0,
        76.0,
        anchor="nw",
        text=keydateServer,
        fill="#FFFFFF",
        font=("IrishGrover Regular", 12 * -1)
    )

    #cerrar ventana
    path = resource_path("assets/frame1/image_2.png")
    image_image_2 = PhotoImage(
        file=path)
    image_2 = canvasbot.create_image(
        826.9999389648438,
        15.0,
        image=image_image_2
    )
    canvasbot.tag_bind(image_2, "<Button-1>", cerrar_ventana_bot)

    #Discord
    path = resource_path("assets/frame1/image_3.png")
    image_image_3 = PhotoImage(
    file=path)
    image_3 = canvasbot.create_image(
    794.9999923706055,
    15.0,
    image=image_image_3
    )
    canvasbot.tag_bind(image_3, "<Button-1>", Abrir_Enlace_Discord)

    #Combate
    path = resource_path("assets/frame1/button_1.png")
    button_image_1 = PhotoImage(
        file=path)
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=mostrar_combate,
        relief="flat"
    )
    button_1.place(
        x=25.0,
        y=196.0,
        width=115.91412353515625,
        height=20.5797119140625
    )

    #PararBot
    path = resource_path("assets/frame1/button_4.png")
    button_image_4 = PhotoImage(
        file=path)
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=PararBot,
        relief="flat"
    )
    button_4.place(
        x=25.0,
        y=265.0,
        width=115.91412353515625,
        height=20.5797119140625
    )


    
    #Capturar
    path = resource_path("assets/frame1/button_2.png")
    button_image_2 = PhotoImage(
        file=path)
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=mostrar_cazar,
        relief="flat"
    )
    button_2.place(
        x=25.0,
        y=229.0,
        width=115.91412353515625,
        height=20.5797119140625
    )
    #Farmeo
    path = resource_path("assets/frame1/button_3.png")
    button_image_3 = PhotoImage(
        file=path)
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=mostrar_farmeo,
        relief="flat"
    )
    button_3.place(
        x=25.0,
        y=160.0,
        width=115.91412353515625,
        height=20.5797119140625
    )
    # definimos los botones como global para acceder a ellos desde cualquier lugar
    global boton_torre_duodraco_teselia, boton_capturar_magikarps_hoeen, boton_pueblo_arenisca_teselia, boton_exp_tentacruel_hoeen, boton_capturar_shinny_mienshao
    global boton_terremoto_automatico, boton_farmeo_cacheo_luvdisc, boton_farmeo_MonAmuleto_Kanto, boton_farmeo_kanto_zona_safari_magikarp
    global boton_capturar_meowths_kanto,boton_capturar_gible_shinno,boton_capturar_whismur_hoeen
    # Botones específicos para el frame de Combate
    boton_torre_duodraco_teselia = tk.Button(windowbot, text=traducted_msg.get('texto_btn_torre_duodraco'), 
                                             command=lambda: IntentoDePescarEnHilo(type=5))

    boton_pueblo_arenisca_teselia = tk.Button(windowbot, text=traducted_msg.get('texto_btn_pueblo_arenisca'), 
                                              command=lambda: IntentoDePescarEnHilo(type=4))
    
    boton_torre_duodraco_teselia.pack_forget()
    boton_pueblo_arenisca_teselia.pack_forget()

    # Botones específicos para el frame de Farmeo 
    boton_exp_tentacruel_hoeen = tk.Button(windowbot, text=traducted_msg.get('texto_btn_exp_tentacruel'), 
                                           command=lambda: IntentoDeMatarTentacruelEnHilo())
    
    boton_terremoto_automatico = tk.Button(windowbot, text=traducted_msg.get('texto_btn_ladron_luvdisc'), 
                                           command=lambda: IntentoDePescarEnHilo(type=2))
    
    boton_farmeo_cacheo_luvdisc = tk.Button(windowbot, text=traducted_msg.get('texto_btn_cacheo_luvdisc'),
                                            command=lambda: IntentoDePescarEnHilo(type=3))
    
    boton_farmeo_MonAmuleto_Kanto = tk.Button(windowbot, text=traducted_msg.get('texto_btn_MonAmuleto_Kanto'), 
                                              command=lambda: IntentoDeLadronAMeowthEnHilo())
    boton_exp_tentacruel_hoeen.pack_forget()
    boton_terremoto_automatico.pack_forget()
    boton_farmeo_cacheo_luvdisc.pack_forget()

    # Botones específicos para el frame de Capturar         "capturar_shinny_mienshao": "Captuar Shinny Mienshao"
    

    boton_capturar_magikarps_hoeen = tk.Button(windowbot, text=traducted_msg.get('texto_btn_capturar_magikarps_hoeen'), 
                                               command=lambda: IntentoDePescarEnHilo(type=1))
    boton_capturar_shinny_mienshao = tk.Button(windowbot, text=traducted_msg.get('capturar_shinny_mienshao'), 
                                               command=lambda: IntentoDeDulceAromaEnHilo())
    boton_farmeo_kanto_zona_safari_magikarp = tk.Button(windowbot, text="magikarps zona safari", 
                                               command=lambda: IntentoDePescarEnHilo(type=6))
    boton_capturar_meowths_kanto = tk.Button(windowbot, text="Meowth Kanto", 
                                            command=lambda: IntentoDeCapturarMeowthEnHilo())
    boton_capturar_gible_shinno = tk.Button(windowbot, text="Gible Shinno", 
                                            command=lambda: IntentoDeCapturarGibleEnHilo())
    boton_capturar_whismur_hoeen = tk.Button(windowbot, text="Whismur Hoeen", 
                                            command=lambda: IntentoDeCapturarWhismurEnHilo())
    boton_capturar_meowths_kanto.pack_forget()
    boton_capturar_gible_shinno.pack_forget()
    boton_capturar_whismur_hoeen.pack_forget()
    boton_capturar_magikarps_hoeen.pack_forget()
    boton_capturar_shinny_mienshao.pack_forget()

    #imagen de fondo
    path = resource_path("assets/frame1/image_4.png")
    image_image_4 = PhotoImage(
        file=path)
    image_4 = canvasbot.create_image(
        504.0,
        355.0,
        image=image_image_4
    )


    global ZanamaUsed,ItemsAdquired,CatchesDone,PokeballsUsed

    # Variable global
    global variable_global
    variable_global = tk.BooleanVar()
    variable_global.set(False)  # Valor inicial

    
    # Función que se ejecuta al hacer clic en el checkbox
    global checkbox
    checkbox = tk.Checkbutton(windowbot, text="Usar Zanama", variable=variable_global, command=cambiar_valor)
    checkbox.config(bg='#0c1c2c',fg="Red", font=('IrishGrover Regular', 16 * -1))  # Cambiar el color de fondo, texto, fuente y tamaño aquíí
    checkbox.place(x=7,y=426)
    checkbox.bind("<Enter>", mostrar_info)

    ZanamaUsed = canvasbot.create_text(
        29.0,
        456.0,
        anchor="nw",
        text="Zanama: 0",
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    ItemsAdquired = canvasbot.create_text(
        29.0,
        486.0,
        anchor="nw",
        text="Items: 0",
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    CatchesDone = canvasbot.create_text(
        29.0,
        516.0,
        anchor="nw",
        text="Catches: 0",
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    PokeballsUsed = canvasbot.create_text(
        29.0,
        546.0,
        anchor="nw",
        text="Pokeballs: 0",
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    global console_text
    # Crear un widget de texto para mostrar la salida de la consola
    console_text = tk.Text(windowbot, wrap="word", bg="black", fg="white", width=80,height=20)
    console_text.place(x=240,y=380)

    # Redirigir la salida de la consola al widget de texto
    text_to_console(console_text)
    
    # Ejecutamos hilo secundario para checkear sesion
    sesion_thread = threading.Thread(target=verificar_sesion)
    sesion_thread.daemon = True  # El hilo se detendrá cuando el programa principal se cierre
    sesion_thread.start()

    windowbot.resizable(False, False)
    windowbot.mainloop()



# Función para enviar texto a la consola
def Send_Texto_To_Console(msg=""):
    global nTextosenpantalla

    hora_actual = datetime.datetime.now().strftime("[%H:%M:%S]")
    mensaje_con_hora = hora_actual + msg

    console_text.config(state="normal")
    console_text.insert(tk.END, mensaje_con_hora + "\n")
    console_text.config(state="disabled")
    nTextosenpantalla += 1
    
    if nTextosenpantalla % 15 == 0: ## clear the console every 15 lines
        console_text.config(state="normal")
        console_text.delete(1.0, tk.END)
        console_text.config(state="disabled")
        nTextosenpantalla = 0


def abrir_interfaz_login():
    global window
    window = tk.Tk()
    window.title("7ls2Dej2mxD92k3")

    window.overrideredirect(True)

    window.bind("<ButtonPress-1>", lambda event: on_drag_start_window(window,event))
    window.bind("<B1-Motion>", lambda event: move_window(window, event))

    window_width = 780
    window_height = 550
    window.configure(bg = "#FFFFFF")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.attributes("-topmost", True)
    global canvaslogin
    canvaslogin = Canvas(
        window,
        bg = "#FFFFFF",
        height = 550,
        width = 780,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvaslogin.place(x = 0, y = 0)

    #Logo izquierda
    path = resource_path("assets/frame0/image_1.png")
    image_image_1 = PhotoImage(file=path)
    image_1 = canvaslogin.create_image(155.0,275.0,image=image_image_1)


    #Registro web
    path = resource_path("assets/frame0/button_1.png")
    button_image_1 = PhotoImage(file=path)

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Abrir_Registro_Web,
        relief="flat"
    )
    
    button_1.place(x=37.0,y=498.0,width=236.0,height=40.5797119140625)

    #Parte Derecha
    path = resource_path("assets/frame0/image_2.png")
    image_image_2 = PhotoImage(file=path)
    image_2 = canvaslogin.create_image(545.0,276.0,image=image_image_2)


    #Entrys
    path = resource_path("assets/frame0/entry_1.png")
    entry_image_1 = PhotoImage(file=path)
    entry_bg_1 = canvaslogin.create_image(557.5,281.5,image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#B7B7B7",fg="#000716",highlightthickness=0)
    entry_1.place(x=464.5,y=268.0,width=186.0,height=25.0)

    path = resource_path("assets/frame0/entry_2.png")
    entry_image_2 = PhotoImage(file=path)
    entry_bg_2 = canvaslogin.create_image(557.5,327.5,image=entry_image_2)
    entry_2 = Entry(bd=0,bg="#B7B7B7",fg="#000716",highlightthickness=0, show="*")
    entry_2.place(x=464.5,y=314.0,width=186.0,height=25.0)

    #Boton de login
    path = resource_path("assets/frame0/button_2.png")
    button_image_2 = PhotoImage(file=path)
    button_2 = Button(image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: login(entry_1.get(),entry_2.get()),
        relief="flat"
    )
                
    button_2.place(
        x=495.5728759765625,
        y=354.0,
        width=128.4271240234375,
        height=44.43428039550781
    )

    #cerrar programa
    path = resource_path("assets/frame0/image_3.png")
    image_image_3 = PhotoImage(file=path)
    image_3 = canvaslogin.create_image(761.0,15.0,image=image_image_3)
    canvaslogin.tag_bind(image_3, "<Button-1>", cerrar_ventana_login)

    #patcher
    path = resource_path("assets/frame0/image_4.png")
    image_image_4 = PhotoImage(file=path)
    image_4 = canvaslogin.create_image(734.0,16.0,image=image_image_4)
    canvaslogin.tag_bind(image_4, "<Button-1>", Patcher)

    #discord
    path = resource_path("assets/frame0/image_5.png")
    image_image_5 = PhotoImage(file=path)
    image_5 = canvaslogin.create_image(707.0,16.0,image=image_image_5)
    canvaslogin.tag_bind(image_5, "<Button-1>", Abrir_Enlace_Discord)

    #Texto Password
    canvaslogin.create_text(
        461.0,
        295.0,
        anchor="nw",
        text=traducted_msg.get('texto_password'),
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )
    # Texto Username
    canvaslogin.create_text(
        461.0,
        247.0,
        anchor="nw",
        text=traducted_msg.get('texto_username'),
        fill="#FFFFFF",
        font=("IrishGrover Regular", 16 * -1)
    )

    #texto de error
    global error_label
    error_label = tk.Label(window, text="",bg="black",fg="red")
    error_label.place(x=495.5,y=436)

    window.resizable(False, False)
    window.mainloop()

def login(username="", password=""):

    global current_version,token,permisos_premium,keydateServer,NickNameServer,PremiumServer
    response = requests.post(SERVER_URL +"/validar_login", json={"username": username, "password": password, "version": current_version})

    time.sleep(3)
    if not username.strip() or not password.strip() or ' ' in username or ' ' in password:
        error_label.config(text=traducted_msg.get('texto_error_texto_en_blanco'))
        return
    
    #sacamos nombre
    NickNameServer = username
    keydateServer = "None"

    if response.status_code == 200:
        data = response.json()

        if not data.get('SameVersion'):
            error_label.config(text=traducted_msg.get('texto_error_desactualizado'))
        else:
            if data.get('valid') is True:
                token = data.get('token')  # Sacamos token y guardamos en memoria

                if data.get('permisos') is True:
                    keydateServer = data.get('dTimeExpire')
                    PremiumServer = "Premium"
                    permisos_premium = True
                else:
                    PremiumServer = "Free"
                    permisos_premium = False

                window.destroy()
                AbrirInterfazBot()
            else:
                error_label.config(text=traducted_msg.get('texto_error_error_password'))
    else:
        error_label.config(text=traducted_msg.get('texto_error_server_mantenimiento'))



def verificar_sesion():
    global NickNameServer, token
    while True:
        payload = {'username': NickNameServer}
        headers = {'Authorization': f'{token}'}

        response = requests.post(SERVER_URL + "/verificar_sesion", data=payload, headers=headers)
        
        if response.status_code != 200:
            os._exit(0)
        
        time.sleep(2.5)  # wait 60 seconds before next verification

def handle_exit(username, token): # function to disconnect user from server
    payload = {'username': username}

    headers = {'Authorization': f'{token}'}
    
    response = requests.post(SERVER_URL + "/logout", data=payload, headers=headers)


def main():  
    EstaActualizado = CheckVersion() # do not allow user to use problem if this is not enabled
    if EstaActualizado == False:
        sys.exit()

    #cargamos json
    global archivo_config
    load_config(archivo_config)
     
    

    if not verificar_tesseract(): # necesary to run the bot
        instalar_tesseract()
        sys.exit(1)
    
    pyautogui.FAILSAFE = True
    #Login Interface
    abrir_interfaz_login()

if __name__ == "__main__":
    main()