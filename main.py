from tkinter import *
import screen_brightness_control as sbc

DEFAULT_BRIGHTNESS = sbc.get_brightness()
MIN = 0 # min do brilho
MAX = 100 # max do brilho
monitor_dict = sbc.list_monitors_info() # infomarçoes da tela

# Funções
def set_brightness(val):
    sbc.set_brightness(val)
    update_brightness_label()

def update_brightness_label():
    brightness = sbc.get_brightness()
    brightness_label.config(text=f"Brilho atual: {brightness}%")

def while_brightness_update():
    brightness = sbc.get_brightness()
    if brightness != pegar_brilho.get():
        set_brightness(pegar_brilho.get())
    master.after(550, while_brightness_update) # 500 ms de delay para atualizar o briho

master = Tk()
master.title("Controlar Brilho da Tela")
master.geometry("400x400")

pegar_brilho = Scale(master, from_=MIN, to=MAX, orient=HORIZONTAL, command=set_brightness, length=300)
pegar_brilho.set(DEFAULT_BRIGHTNESS)
pegar_brilho.pack()

brightness_label = Label(master, text=f"Brilho atual: {DEFAULT_BRIGHTNESS}%", font=("Arial", 14))
brightness_label.pack(pady=20)

n_monitor = monitor_dict[0]['name']
info_monitor = monitor_dict[0]['model']
serial_monitor = monitor_dict[0]['serial']
manufacturer_monitor = monitor_dict[0]['manufacturer']

monitor_info_label = Label(master, text=f"{n_monitor}", font=("Arial", 10))
monitor_info_label2 = Label(master, text=f"{info_monitor}", font=("Arial", 10))
monitor_info_label3 = Label(master, text=f"{serial_monitor}", font=("Arial", 10))
monitor_info_label4 = Label(master, text=f"{manufacturer_monitor}", font=("Arial", 10))

monitor_info_label.pack()
monitor_info_label2.pack()
monitor_info_label3.pack()
monitor_info_label4.pack()
while_brightness_update()

mainloop()

monitor = sbc.list_monitors_info()
