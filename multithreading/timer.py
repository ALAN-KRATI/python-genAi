import threading
import time

def timer():
    while True:
        print("System alive...")
        time.sleep(2)

t = threading.Thread(target=timer)
t.start()