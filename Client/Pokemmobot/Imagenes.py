import pytesseract
import pyautogui
import time
from PIL import Image

def buscar_texto_en_pantalla(texto, imagen_pantalla, debug = False):
    # use tesseract to get text
    screen_text = pytesseract.image_to_string(Image.open(imagen_pantalla))
    if debug == True:
        print(screen_text)

    # Comprueba si esta el texto pero aveces falla
    if texto.lower() in screen_text.lower():
        return True
    else:
        return False

def capturar_pantalla(width, height, topvalue, leftvalue):
    screen_width, screen_height = pyautogui.size()

    left = (screen_width - width) // 2 - leftvalue
    top = (screen_height - height) // 2 - topvalue  

    if 0 < width <= screen_width and 0 < height <= screen_height:
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot.save("screenshot.png")
        return "screenshot.png"
    else:
        return None
    
def verificar_texto_en_pantalla(texto_a_buscar,x,y, valueHeigh, valueCorner = 0, debug = False):
    # Captura la pantalla
    imagen_pantalla = capturar_pantalla(x, y, valueHeigh, valueCorner)

    time.sleep(0.3)  # Ajustare mas tarde

    resultado = buscar_texto_en_pantalla(texto_a_buscar, imagen_pantalla, debug)

    return resultado