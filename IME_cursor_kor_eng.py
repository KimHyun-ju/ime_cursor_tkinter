import atexit
import ctypes
import tkinter as tk
from threading import Thread
import pystray
from PIL import Image

class IME_cursor_kor_eng(tk.Tk):
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    def __init__(self):
        super().__init__()
        atexit.register(self.close_func)
        self.overrideredirect(1)
        self.wm_attributes("-topmost", 1)
        self['bg'] = "#2b2b2b"
        self.geometry(f"16x16")
        self.wm_attributes("-transparentcolor", "#2b2b2b")
        if ime_state():
            self.label = tk.Label(self, text="가", bg="#2b2b2b", font='bold', fg='#74FF1E')
        else:
            self.label = tk.Label(self, text="a", bg="#2b2b2b", font='bold', fg="#ff0000")
        self.label.pack(fill="both", expand=True)
        self.t1 = Thread(target=self.cursor)
        self.t2 = Thread(target=self.set_label)
        self.t1.start()
        self.t2.start()

    def set_label(self):
        if ime_state():
            self.label.configure(text='가', fg= "#74FF1E")
        else:
            if is_capslock_on():
                self.label.configure(text='A', fg="#ff0000")
            else:
                self.label.configure(text='a', fg= "#ff0000")
        self.label_state = self.after(50, self.set_label)

    def cursor(self):
        cursorpos=self.POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(cursorpos))
        self.geometry(f"+{cursorpos.x+5}+{cursorpos.y-8}")
        self.cursor_state = self.after(1, self.cursor)

    def close_func(self):
        try:
            self.after_cancel(self.cursor_state)
            self.after_cancel(self.label_state)
            self.destroy()
        except:
            pass

def ime_state():
    hIME = ctypes.windll.imm32.ImmGetDefaultIMEWnd(ctypes.windll.user32.GetForegroundWindow())
    if hIME:
        return ctypes.windll.user32.SendMessageW(hIME, 0x0283, 0x0005, 0)
        # WM_IME_CONTROL, IMC_GETOPENSTATUS = 0x0283, 0x0005

def is_capslock_on():
    return True if ctypes.windll.user32.GetKeyState(0x14) else False

def quit_window(icon, item):
    # https://stackoverflow.com/questions/54835399/running-a-tkinter-window-and-pystray-icon-together
    icon.visible = False
    icon.stop()
    root.quit()

def show_window(icon, item):
    root.after(0, root.deiconify)

def stop_window(icon, item):
    root.withdraw()

if __name__ == "__main__":
    root = IME_cursor_kor_eng()
    image = Image.open("image.ico")
    menu = (pystray.MenuItem('Quit', quit_window),
            pystray.MenuItem('Stop', stop_window),
            pystray.MenuItem('Show', show_window))
    icon = pystray.Icon("name", image, "title", menu)
    icon.run_detached()
    root.mainloop()
    # pyinstaller -w --icon=image.ico --add-data "image.ico;." IME_cursor_kor_eng.py
