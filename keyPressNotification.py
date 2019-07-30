from win32api import GetKeyState 
import keyboard 
from win10toast import ToastNotifier

notif = ToastNotifier()

keyboard.add_hotkey('capslock',lambda:notif.show_toast("Notofication","Caps lock pressed",duration=1.5))
keyboard.add_hotkey('numlock',lambda:notif.show_toast("Notofication","Num lock pressed",duration=1.5))

#end the program
keyboard.wait('ctrl+shift+q') 
