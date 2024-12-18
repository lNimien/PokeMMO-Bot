import pyautogui
import pydirectinput
import time
import pytesseract
from PIL import Image
import threading
import keyboard
import re
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

ejecucion = True  # variable local to check the execute of the bot

def key_control():
    global ejecucion
    while True:
        if keyboard.is_pressed('f7'):
            sys.exit()
        if keyboard.is_pressed('f9'):
            ejecucion = False  # stop execute
            print("Programa detenido...")
            while True:
                if keyboard.is_pressed('f10'):
                    ejecucion = True  # force back to work
                    print("Programa reanudado...")
                    break  
        time.sleep(0.2)  # reduce cpu usage

def find_text_in_screen(type, texto, imagen_pantalla):
    if type == 1:
        texto_pantalla = pytesseract.image_to_string(Image.open(imagen_pantalla))
        return texto.lower() in texto_pantalla.lower()

    elif type == 2:
        texto_pantalla = pytesseract.image_to_string(Image.open(imagen_pantalla)).lower()
        texto_lower = texto.lower()
        return sum(1 for _ in re.finditer(rf'\b{texto_lower}\b', texto_pantalla))

    elif type == 3:
        texto_pantalla = pytesseract.image_to_string(Image.open(imagen_pantalla)).lower()

        # verify if there is numbers
        if any(c.isdigit() or c == '.' for c in texto_pantalla):
            texto_pantalla_numerico = re.sub(r'[^\d.]', '', texto_pantalla)
            try:
                return int(texto_pantalla_numerico)
            except ValueError:
                pass  # failed

        return 10000000  # if not a number return a bigger number

def make_screenshoot(width, height, topvalue, leftvalue):
    screen_width, screen_height = pyautogui.size()

    left = (screen_width - width) // 2 - leftvalue
    top = (screen_height - height) // 2 - topvalue  

    if 0 < width <= screen_width and 0 < height <= screen_height:
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot.save("screenshot.png")
        return "screenshot.png"
    else:
        print("size incorrectly.")
        return None
    
def check_text_in_Screen(texto_a_buscar,x,y, valueHeigh, valueCorner = 0, type = 1):
    # Captura la pantalla
    imagen_pantalla = make_screenshoot(x, y, valueHeigh, valueCorner)

    if type < 2:
        time.sleep(0.3)  # adjust accordingly

    # search for text in the screenshot
    resultado = find_text_in_screen(type, texto_a_buscar, imagen_pantalla)

    if type == 3:
        return int(resultado)
    
    return resultado



#################################
########### FUNCIONES ###########
#################################

def Objects():
    pydirectinput.click(1227, 295)

    ItsGoodPrice = check_text_in_Screen("31", 101,35,152,-40,3) #return price
    time.sleep(0.7)
    print(ItsGoodPrice)
    if ItsGoodPrice < 6000 or ItsGoodPrice > 7600: #lets avoid buying things that are too cheap or too expensive
        return

    print("Tengo 1x31")
    print(ItsGoodPrice)
    if ItsGoodPrice < 6850:
        pydirectinput.click(1306, 394) # buy button
        time.sleep(0.2)
        pydirectinput.click(1084, 498)
        time.sleep(0.2)
        pydirectinput.click(961, 533) # confirm button
        print("hay que comprarlo")
    else:
        print("Es demasiado caro")
        

        
    time.sleep(1)
    ItsGoodPrice = 0

def pokemonsv1():
    time.sleep(0.1)
    pydirectinput.click(1227, 295)

    ItsGoodPrice = check_text_in_Screen("31", 101,35,152,-90,3) #devuelve el valor

    if ItsGoodPrice < 1500 or ItsGoodPrice > 4000: #lets avoid buying things that are too cheap or too expensive
        return

    print(ItsGoodPrice)
    if ItsGoodPrice < 2001:
        time.sleep(0.1)
        pydirectinput.click(1339, 385) # buy button
        time.sleep(0.3)
        pydirectinput.click(961, 549) # confirm button
        print("hay que comprarlo")
    else:
        print("Es demasiado caro")

    
    time.sleep(0.2)
    ItsGoodPrice = 0

def Pokemons():
    pydirectinput.click(1227, 295)

    Have31 = check_text_in_Screen("31", 194,44,152,50,2) # 31 IV
    time.sleep(0.2)
    xHave31 = check_text_in_Screen("31", 194,44,152,50,2) # 31 IV
    time.sleep(0.2)
    print(f"How many 31 do you have {Have31} , Second {xHave31}")
    if Have31 == 1 and xHave31 == 1:
        ItsGoodPrice = check_text_in_Screen("31", 101,35,152,-90,3) 
        time.sleep(0.3)

        if ItsGoodPrice < 1500 or ItsGoodPrice > 4000: #lets avoid buying things that are too cheap or too expensive
            return

        print(ItsGoodPrice)
        if ItsGoodPrice < 2001:
            pydirectinput.click(1339, 385) # buy button
            time.sleep(0.2)
            pydirectinput.click(961, 549)   # confirm button
        else:
            print("to expensive")

        
    time.sleep(0.5)
    ItsGoodPrice = 0


## testing functions 
def mostrar_posicion():
    try:
        while True:
            time.sleep(.5)
            x, y = pyautogui.position()
            print(f"Posición del ratón - X: {x}, Y: {y}")
    except KeyboardInterrupt:
        print("Terminando el seguimiento de la posición del ratón.")
    
def testing():
    time.sleep(1)
    CheckPrice = check_text_in_Screen('Gible', 1351 ,85, 380)
    print(CheckPrice)
#################################


def main():
    pyautogui.FAILSAFE = True
    # mt to control keys F9 and F10
    keyboard_thread = threading.Thread(target=key_control)
    keyboard_thread.start()
    #testing
    #mostrar_posicion()
    #testing()
    pyautogui.FAILSAFE = True
    while True:
        global ejecucion
        if ejecucion:
             Objects()  
        else:
            time.sleep(0.5)  # Espera para reducir el uso de la CPU si el programa está detenido"""


if __name__ == "__main__":
    main()