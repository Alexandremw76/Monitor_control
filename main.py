from tkinter import *
import screen_brightness_control as sbc

DEFAULT_BRIGHTNESS = sbc.get_brightness()
MIN = 0 # min do brilho
MAX = 100 # max do brilho
monitor_dict = sbc.list_monitors_info() # infomarçoes da tela

# Funções
def on_scale_move():
     while_brightness_update() 

def set_brightness():
    val = barra_de_brilho.get()
    sbc.set_brightness(val)
    update_brightness_label()

def update_brightness_label():
    brightness = sbc.get_brightness()
    brightness_label.config(text=f"Brilho atual: {brightness}%")

def while_brightness_update():
    brightness = sbc.get_brightness()
    if brightness[0] != barra_de_brilho.get():
        set_brightness()
    master.after(500, while_brightness_update) # 500 ms de delay para atualizar o briho

def retry():
    set_brightness()  

master = Tk()
master.title("Controlar Brilho da Tela")
master.geometry("400x400")

barra_de_brilho = Scale(master, from_=MIN, to=MAX, orient=HORIZONTAL, length=300)# barra de brilho
barra_de_brilho.set(DEFAULT_BRIGHTNESS)
barra_de_brilho.pack()

brightness_label = Label(master, text=f"Brilho atual: {DEFAULT_BRIGHTNESS}%", font=("Arial", 14))
brightness_label.pack(pady=20)

retry_button = Button(master,text ="Retry to Set Brightness",command=retry())
retry_button.pack()


n_monitor = monitor_dict[0]['name']
info_monitor = monitor_dict[0]['model']
manufacturer_monitor = monitor_dict[0]['manufacturer']

monitor_info_label = Label(master, text=f"{n_monitor}", font=("Arial", 10))
monitor_info_label2 = Label(master, text=f"{info_monitor}", font=("Arial", 10))
monitor_info_label4 = Label(master, text=f"{manufacturer_monitor}", font=("Arial", 10))
monitor_info_label.pack()
monitor_info_label2.pack()
monitor_info_label4.pack()
while_brightness_update()
barra_de_brilho.update()

mainloop()
