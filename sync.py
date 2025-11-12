import subprocess
import time

try:
    import pyautogui as agui
    from tkinter import ttk
    import tkinter
except ImportError:
    print("Bibliotecas nao encontradas. Instalando...")
    try:
        subprocess.run(['python', '-m', 'pip', 'install', 'pyautogui', 'tkinter'],check=False)
    except Exception:
        subprocess.run(['py', '-m', 'pip', 'install', 'pyautogui', 'tkinter'],check=False)

import pyautogui as agui
from tkinter import ttk
import tkinter

def wait_until(target_time):
    while True:
        current_time = time.time()
        if current_time >= target_time:
            break
        time.sleep(0.01)
    print("Tempo de execuçao:", time.ctime(target_time))

def main(move_x=None, move_y=None,horas=None,minutos=None,segundos=None):
    now = time.localtime()
    target_time = time.mktime((
        now.tm_year, now.tm_mon, now.tm_mday,
        horas,minutos,segundos,
        now.tm_wday, now.tm_yday, now.tm_isdst
    ))

    print("Esperando ate:", time.ctime(target_time))
    wait_until(target_time)
    print("Começando execuçao:", time.ctime())

    agui.moveTo(move_x, move_y)
    agui.click()


if __name__ == "__main__":

    while(True):
        root = tkinter.Tk()
        root.title("Agendador de Click")
        frame = ttk.Frame(root, padding="10")
        frame.grid()
        ttk.Label(frame, text="Coordenada X:").grid(column=0, row=0)
        x_entry = ttk.Entry(frame)
        x_entry.grid(column=1, row=0)
        ttk.Label(frame, text="Coordenada Y:").grid(column=0, row=1)
        y_entry = ttk.Entry(frame)
        y_entry.grid(column=1, row=1)
        ttk.Label(frame, text="Horas (0-23):").grid(column=0, row=2)
        horas_entry = ttk.Entry(frame)
        horas_entry.grid(column=1, row=2)
        ttk.Label(frame, text="Minutos (0-59):").grid(column=0, row=3)
        minutos_entry = ttk.Entry(frame)
        minutos_entry.grid(column=1, row=3)
        ttk.Label(frame, text="Segundos (0-59):").grid(column=0, row=4)
        segundos_entry = ttk.Entry(frame)
        segundos_entry.grid(column=1, row=4)
        def on_submit():
            move_x = int(x_entry.get())
            move_y = int(y_entry.get())
            horas = int(horas_entry.get())
            minutos = int(minutos_entry.get())
            segundos = int(segundos_entry.get())
            root.destroy()
            main(move_x, move_y, horas, minutos, segundos)
        submit_button = ttk.Button(frame, text="Agendar Click", command=on_submit)
        submit_button.grid(column=0, row=5, columnspan=2)
        root.mainloop()
    print("Programa encerrado.")


