import json, lz4.block, time, pyautogui, datetime

data1 = datetime.datetime.now()
minutes = 0
print(data1)

while minutes < 20:

    f = open("C:/Users/Vinicius/AppData/Roaming/Mozilla/Firefox/Profiles/wb3o4y6g.default-release/sessionstore-backups/recovery.jsonlz4", "rb")

    magic = f.read(8)
    data = json.loads(lz4.block.decompress(f.read()).decode('utf-8'))
    f.close()
    current_window = ""
    print(data)

    data2 = datetime.datetime.now()
    diff = data2 - data1
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    for win in data.get("windows"):
            for tab in win.get("tabs"):
                i = int(tab.get("index")) - 1
                current_window = tab.get("entries")[i].get("url")
                time.sleep(3)
            print(current_window)
    if "https://www.youtube.com/" in str(current_window):
            print("yes")
            pyautogui.hotkey('ctrl', 'f4')
            time.sleep(30)
    elif"https://web.facebook.com/?_rdc=1&_rdr"in str(current_window):
            print("yes")
            pyautogui.hotkey('ctrl', 'f4')
            time.sleep(30)
    else:
            print("não")

print(minutes)