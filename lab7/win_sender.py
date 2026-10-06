import win32gui
import win32con
import sys

WM_MY_COMMAND = win32con.WM_USER + 1337

print("[ОТПРАВИТЕЛЬ] Ищем окно приемника по зарегистрированному имени класса...")
# Функция FindWindow делает запрос к подсистеме win32k ядра ОС Windows
hwnd = win32gui.FindWindow("SysProgHiddenReceiverClass", None)

if hwnd == 0:
    print("[ОШИБКА] Окно приемника не найдено в системе! Запустите сначала win_receiver.py.")
    sys.exit(1)

print(f"[ОТПРАВИТЕЛЬ] Цель найдена. HWND приемника: {hwnd}")
print("[ОТПРАВИТЕЛЬ] Вызываем SendMessage: отправляем синхронный сигнал 777...")

# Системный вызов SendMessage блокирует поток отправителя до обработки сообщения
win32gui.SendMessage(hwnd, WM_MY_COMMAND, 777, 0)

print("[ОТПРАВИТЕЛЬ] Сообщение обработано получателем. Конец работы.")