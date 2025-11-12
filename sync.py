import time
import pyautogui as agui


def wait_until(target_time):
    while True:
        current_time = time.time()
        if current_time >= target_time:
            break
        time.sleep(0.01)
    print("Tempo de execuçao:", time.ctime(target_time))

if __name__ == "__main__":

    #Move cursor to x=100 y=100
    move_x = 100
    move_y = 100
    agui.moveTo(move_x, move_y)
    agui.click()

    horas = 12
    minutos = 31
    segundos = 0

    now = time.localtime()
    target_time = time.mktime((
        now.tm_year, now.tm_mon, now.tm_mday,
        12, 31, 0,
        now.tm_wday, now.tm_yday, now.tm_isdst
    ))

    print("Esperando ate:", time.ctime(target_time))
    wait_until(target_time)
    print("Começando execuçao:", time.ctime())

