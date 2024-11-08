import pyautogui
import keyboard
import threading
import time
import random
import os

# Флаг для управления движением мыши
active = False

def move_mouse():
    global active
    while True:
        if active:
            # Получаем текущие координаты курсора
            x, y = pyautogui.position()
            # Случайные смещения
            dx = random.randint(-20, 20)
            dy = random.randint(-20, 20)
            # Перемещаем мышь
            pyautogui.moveRel(dx, dy, duration=0.1)
            time.sleep(1)  # Задержка между движениями

def start_moving():
    global active
    active = True
    print("Мышь начала двигаться.")

def stop_moving():
    global active
    active = False
    print("Движение мыши остановлено.")


# Слушаем сочетания клавиш
keyboard.add_hotkey('shift+f8', start_moving)
keyboard.add_hotkey('shift+f12', stop_moving)
keyboard.add_hotkey('shift+ctrl+f12', lambda: os._exit(0))

# Запускаем поток для движения мыши
thread = threading.Thread(target=move_mouse, daemon=True)
thread.start()

start_moving()

# Основной поток просто ждет
keyboard.wait()
