import os
import sys
sys.path.append('C:\\Users\\stefa\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages')
import pyautogui
import tkinter as tk
from ctypes import windll, byref, c_int
import configparser

# Funzione per ottenere il percorso delle risorse, considerando se il codice è in esecuzione come eseguibile
def resource_path(relative_path):
    try:
        # Per PyInstaller, i file sono estratti temporaneamente
        base_path = sys._MEIPASS
    except Exception:
        # Se non è un eseguibile, usa il percorso relativo normale
        base_path = os.path.dirname(__file__)
    
    return os.path.join(base_path, relative_path)

def press_keys(combination, state_label, change_color=True, bypass_alt_tab=False):
    pyautogui.hotkey(*combination)
    if change_color:
        toggle_state(state_label)
    if alt_tab_after_combination and bypass_alt_tab == False:
        pyautogui.hotkey('alt', 'tab')

def toggle_state(label):
    current_color = label.cget("bg")
    new_color = "red" if current_color == "green" else "green"
    label.config(bg=new_color)

def start_drag(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def on_drag(event):
    widget = event.widget
    x = widget.winfo_pointerx() - widget.startX
    y = widget.winfo_pointery() - widget.startY
    widget.winfo_toplevel().geometry(f"+{x}+{y}")

def close_program(event):
    root.destroy()

def round_corners(hwnd, radius):
    """Setta gli angoli della finestra come arrotondati."""
    DWM_WINDOW_CORNER_PREFERENCE = 33

    # Definizione della preferenza per gli angoli arrotondati
    dwm_window_corner_preference = c_int(2)  # 2 = DWMWCP_ROUND

    windll.dwmapi.DwmSetWindowAttribute(
        hwnd,
        DWM_WINDOW_CORNER_PREFERENCE,
        byref(dwm_window_corner_preference),
        c_int(4)  # dimensione in byte della variabile dwm_window_corner_preference
    )

indipendent_button1 = False

def handle_button1():
    """Gestisce il bottone 1."""
    global indipendent_button1  # usa 'global' per modificare la variabile globale

    if discord_logic:
        press_keys(combination1, state_label1, False)
        if state_label1.cget("bg") == "red" and state_label2.cget("bg") == "red":
            state_label1.config(bg="green")
            state_label2.config(bg="green")
            indipendent_button1 = False
        elif state_label1.cget("bg") == "red" and state_label2.cget("bg") == "green":
            state_label1.config(bg="green")
            indipendent_button1 = False
        elif state_label1.cget("bg") == "green" and state_label2.cget("bg") == "green":
            state_label1.config(bg="red")
            indipendent_button1 = True
        elif state_label1.cget("bg") == "green" and state_label2.cget("bg") == "red":
            state_label1.config(bg="red")
            indipendent_button1 = False
    else:
        press_keys(combination1, state_label1)

def handle_button2(bypass_alt_tab = False):
    """Gestisce il bottone 2."""
    global indipendent_button1  # usa 'global' per modificare la variabile globale

    if discord_logic:
        press_keys(combination2, state_label2, False, bypass_alt_tab)
        if state_label1.cget("bg") == "green" and state_label2.cget("bg") == "green":
            state_label1.config(bg="red")
            state_label2.config(bg="red")
            indipendent_button1 = False
        elif state_label1.cget("bg") == "green" and state_label2.cget("bg") == "red":
            state_label2.config(bg="green")
            indipendent_button1 = False
        elif state_label1.cget("bg") == "red" and state_label2.cget("bg") == "green":
            state_label1.config(bg="red")
            state_label2.config(bg="red")
            indipendent_button1 = True
        elif state_label1.cget("bg") == "red" and state_label2.cget("bg") == "red":
            if indipendent_button1 == True:
                state_label2.config(bg="green")
            else:
                state_label1.config(bg="green")
                state_label2.config(bg="green")
    else:
        press_keys(combination2, state_label2, True, bypass_alt_tab)

def handle_button_all():
    handle_button2(True)  # Esegui handle_button2
    press_keys(combination3, state_label3) 

# Leggere il file di configurazione
config = configparser.ConfigParser()
config.read('config.ini')

# Leggere il valore di discord_logic dal file di configurazione
discord_logic = config['Settings'].getboolean('discord_logic')

# Imposta il valore di opacità (0 = totalmente trasparente, 100 = totalmente opaco)
opacity_value = int(config['Settings']['opacity'])
background_color = config['Settings']['background_color']
scale_factor = float(config['Settings']['scale_factor'])
alt_tab_after_combination = config['Settings'].getboolean('alt_tab_after_combination')

# Calcola l'opacità come valore tra 0.0 e 1.0
opacity = opacity_value / 100.0

# Leggere le combinazioni di tasti
combination1 = config['KeyCombinations']['combination1'].split(', ')
combination2 = config['KeyCombinations']['combination2'].split(', ')
combination3 = config['KeyCombinations']['combination3'].split(', ')

def scale_size(size):
    return int(size * scale_factor)

# Creare la finestra principale
root = tk.Tk()
root.title("Toolbar")
root.attributes('-topmost', True)
root.overrideredirect(True)  # Rimuove la barra del titolo
root.config(bg=background_color)  # Imposta il colore di sfondo

# Imposta la trasparenza della finestra
root.attributes('-alpha', opacity)

# Arrotondare i bordi della finestra
hwnd = windll.user32.GetParent(root.winfo_id())
round_corners(hwnd, 20)  # Arrotonda gli angoli della finestra

# Caricare e ridimensionare le icone
def resize_image(image_path, scale_factor):
    image = tk.PhotoImage(file=image_path)
    width = int(image.width() * scale_factor)
    height = int(image.height() * scale_factor)
    return image.subsample(image.width() // width, image.height() // height)

drag_icon = resize_image(resource_path("drag.png"), scale_factor)
close_icon = resize_image(resource_path("close.png"), scale_factor)
microphone_icon = resize_image(resource_path("microphone.png"), scale_factor)
joystick_icon = resize_image(resource_path("joystick.png"), scale_factor)
chat_icon = resize_image(resource_path("chat.png"), scale_factor)
all_icon = resize_image(resource_path("all.png"), scale_factor)  

# Creare un frame per il trascinamento
drag_frame = tk.Frame(root, bg=background_color, width=scale_size(30), height=scale_size(30))
drag_frame.pack(side=tk.LEFT, padx=scale_size(2))

drag_label = tk.Label(drag_frame, image=drag_icon, bg=background_color)
drag_label.pack(fill=tk.BOTH, expand=True)

drag_label.bind("<Button-1>", start_drag)
drag_label.bind("<B1-Motion>", on_drag)

# Spaziatore tra il drag e il primo bottone
spacer_frame = tk.Frame(root, bg=background_color, width=scale_size(10))
spacer_frame.pack(side=tk.LEFT)

# Spaziatore tra il bottone "all" e il tasto close
spacer_before_close = tk.Frame(root, bg=background_color, width=scale_size(10))
spacer_before_close.pack(side=tk.RIGHT)

# Creare un frame per la chiusura
close_frame = tk.Frame(root, bg=background_color, width=scale_size(30), height=scale_size(30))
close_frame.pack(side=tk.RIGHT, padx=scale_size(2))

close_label = tk.Label(close_frame, image=close_icon, bg=background_color)
close_label.pack(fill=tk.BOTH, expand=True)

close_label.bind("<Button-1>", close_program)

# Creare frame per i bottoni e i pallini
button_frame = tk.Frame(root, bg=background_color)
button_frame.pack(side=tk.LEFT)

# Crea i bottoni con le icone e assegna le funzioni
button1 = tk.Button(button_frame, image=microphone_icon, command=handle_button1)
button2 = tk.Button(button_frame, image=chat_icon, command=handle_button2)
button3 = tk.Button(button_frame, image=joystick_icon, command=lambda: press_keys(combination3, state_label3))
button_all = tk.Button(button_frame, image=all_icon, command=handle_button_all) 

# Creare i pallini per gli stati
state_label1 = tk.Label(button_frame, bg="green", width=scale_size(2), height=scale_size(1))
state_label2 = tk.Label(button_frame, bg="green", width=scale_size(2), height=scale_size(1))
state_label3 = tk.Label(button_frame, bg="green", width=scale_size(2), height=scale_size(1))

# Configurare il cambio di stato manuale dei pallini
state_label1.bind("<Button-1>", lambda e: toggle_state(state_label1))
state_label2.bind("<Button-1>", lambda e: toggle_state(state_label2))
state_label3.bind("<Button-1>", lambda e: toggle_state(state_label3))

# Creare spaziatori vuoti dopo i pallini
spacer_after_label1 = tk.Frame(button_frame, bg=background_color, width=scale_size(10))
spacer_after_label2 = tk.Frame(button_frame, bg=background_color, width=scale_size(10))
spacer_after_label3 = tk.Frame(button_frame, bg=background_color, width=scale_size(15))

# Posiziona i bottoni, i pallini e gli spaziatori nella finestra
button1.grid(row=0, column=0, padx=scale_size(5), pady=scale_size(3))
state_label1.grid(row=0, column=1, padx=scale_size(5), pady=scale_size(3))
spacer_after_label1.grid(row=0, column=2, padx=scale_size(2), pady=scale_size(3))

button2.grid(row=0, column=3, padx=scale_size(5), pady=scale_size(3))
state_label2.grid(row=0, column=4, padx=scale_size(5), pady=scale_size(3))
spacer_after_label2.grid(row=0, column=5, padx=scale_size(2), pady=scale_size(3))

button3.grid(row=0, column=6, padx=scale_size(5), pady=scale_size(3))
state_label3.grid(row=0, column=7, padx=scale_size(5), pady=scale_size(3))
spacer_after_label3.grid(row=0, column=8, padx=scale_size(2), pady=scale_size(3))

button_all.grid(row=0, column=9, padx=scale_size(5), pady=scale_size(3))

# Imposta la dimensione e la posizione della finestra 
root.geometry(f"{scale_size(400)}x{scale_size(50)}+100+100")

# Avvia il loop dell'interfaccia grafica 
root.mainloop()