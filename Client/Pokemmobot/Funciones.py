import sys
import subprocess
import webbrowser
import os
import requests
import tkinter as tk

from tkinter import messagebox,Canvas, Entry, Button, PhotoImage
SERVER_IP ="51.210.223.235"
SERVER_PORT = "1345"
SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}"
EnlaceDiscord = "https://discord.gg/9A2DjJvTJz"
current_version = "1.1.5"

def Abrir_Registro_Web(event=None):
    webbrowser.open(SERVER_URL+"/")

def Abrir_Enlace_Discord(event=None):
    webbrowser.open(EnlaceDiscord)

def Patcher(event=None):
    subprocess.Popen(['Updater.exe'])
    sys.exit(1)

    

def move_window(window, event):
    window.geometry(f"+{event.x_root - x}+{event.y_root - y}")


def move_windowbot(windowbot, event):
    windowbot.geometry(f"+{event.x_root - x}+{event.y_root - y}")

def on_drag_start_windowbot(windowbot, event):
    global x, y
    x = event.x_root - windowbot.winfo_x()
    y = event.y_root - windowbot.winfo_y()

def on_drag_start_window( window, event):
    global x, y
    x = event.x_root - window.winfo_x()
    y = event.y_root - window.winfo_y()


def verificar_tesseract():
    try:
        subprocess.run([r'C:\Program Files\Tesseract-OCR\tesseract', '--version'], capture_output=True, check=True)
        #print(mensajes_seleccionados.get('teseract_instalado'))
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def instalar_tesseract():
    try:
        ruta_instalador = os.path.join(os.getcwd(), "tesseract.exe")
        subprocess.run([ruta_instalador], check=True)
        #print(mensajes_seleccionados.get('teseract_instalado'))
        return True
    except subprocess.CalledProcessError:
        #print(mensajes_seleccionados.get('teseract_error'))
        return False

def CheckVersion():
    global error_label

    response = requests.post(SERVER_URL +"/validar_version", json={"version": current_version})
    if response.status_code == 200:
        data = response.json()
        if data.get('CorrectVersion'):
            return True
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Error", "Ejecuta el updater.exe")
            return False
        
