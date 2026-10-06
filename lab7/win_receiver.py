import win32gui
import win32con
import win32process
import os

# Уникальный код нашего пользовательского сообщения
WM_MY_COMMAND = win32con.WM_USER + 1337

def window_procedure(hwnd, msg, wparam, lparam):
    """Низкоуровневая функция — обработчик очереди сообщений ядра"""
    if msg == WM_MY_COMMAND:
        print(f"\n[ПРИЕМНИК] Перехвачено системное сообщение WM_USER+1337!")
        print(f"[ПРИЕМНИК] Параметр команды (WPARAM): {wparam}")
        if wparam == 777:
            print("[ПРИЕМНИК] Сигнал подтвержден. Выполняем экстренное завершение процесса...")
            os._exit(0)
        return 0
    # Все остальные стандартные сообщения Windows отдаем ОС
    return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

# 1. Регистрируем класс окна в Windows API
wc = win32gui.WNDCLASS()
wc.lpfnWndProc = window_procedure
wc.lpszClassName = "SysProgHiddenReceiverClass"
class_atom = win32gui.RegisterClass(wc)

# 2. Создаем скрытое окно (ширина и высота = 0)
hwnd = win32gui.CreateWindow(
    class_atom, "SysProgReceiverWindow",
    0, 0, 0, 0, 0, 0, 0, 0, None
)

print(f"[ПРИЕМНИК] Процесс запущен. Мой PID: {os.getpid()}")
print(f"[ПРИЕМНИК] Ядро Windows выделило нам дескриптор HWND: {hwnd}")
print("[ПРИЕМНИК] Входим в бесконечный системный цикл выборки сообщений GetMessage()...")

# 3. Запускаем бесконечный цикл выборки сообщений (Pump)
win32gui.PumpMessages()