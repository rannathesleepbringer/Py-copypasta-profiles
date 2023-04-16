import keyboard as kb
import pyperclip
from time import sleep

#change prefered function keys. Can't really use convenient combos so a special keyboard may be necessary.
mod1 = "f13"
mod2 = "f14"

#helper function to rewrite the PyperClip for readability. 
class clip:
    def mod(data):
        pyperclip.copy(data)
    def read():
        return pyperclip.paste()
#Main function for saving and restoring clipboard profiles    
class data:
    def store(data):
        kb.send("ctrl+c")
        sleep(0.1)
        global data1
        global data2
        global data3
        global data4
        global data5
        global data6
        global data7
        global data8
        global data9
        
        match data:
            case 1:
                data1=clip.read()
                print(data1)
            case 2:
                data2=clip.read()
                print(data2)
            case 3:
                data3=clip.read()
                print(data3)
            case 4:
                data4=clip.read()
                print(data4)    
            case 5:
                data5=clip.read()
                print(data5)
            case 6:
                data6=clip.read()
                print(data6)
            case 7:
                data7=clip.read()
                print(data7)
            case 8:
                data8=clip.read()
                print(data8)
            case 9:
                data9=clip.read()
                print(data9)
            case _:
                return
            
    def retrieve(data):
        store=clip.read()
        sleep(0.1)
        clip.mod('')
        sleep(0.1)

        match data:
            case 1:
                clip.mod(data1)
            case 2:
                clip.mod(data2)
            case 3:
                clip.mod(data3)
            case 4:
                clip.mod(data4)
            case 5:
                clip.mod(data5)
            case 6:
                clip.mod(data6)
            case 7:
                clip.mod(data7)
            case 8:
                clip.mod(data8)
            case 9:
                clip.mod(data9)
            case _:
                return

        kb.send("ctrl+v")
        clip.mod(store)
#setting keyboard hotkeys        
kb.add_hotkey(mod1+'+1', lambda:data.store(1), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+2', lambda:data.store(2), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+3', lambda:data.store(3), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+4', lambda:data.store(4), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+5', lambda:data.store(5), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+6', lambda:data.store(6), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+7', lambda:data.store(7), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+8', lambda:data.store(8), timeout=1, suppress=True)
kb.add_hotkey(mod1+'+9', lambda:data.store(9), timeout=1, suppress=True)

kb.add_hotkey(mod2+'+1', lambda:data.retrieve(1), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+2', lambda:data.retrieve(2), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+3', lambda:data.retrieve(3), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+4', lambda:data.retrieve(4), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+5', lambda:data.retrieve(5), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+6', lambda:data.retrieve(6), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+7', lambda:data.retrieve(7), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+8', lambda:data.retrieve(8), timeout=2, suppress=True)
kb.add_hotkey(mod2+'+9', lambda:data.retrieve(9), timeout=2, suppress=True)

#exit command
kb.wait("ctrl+escape", suppress=True)
