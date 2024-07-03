import requests
import re

sess = requests.Session()

for i in range(1337):
        res = sess.get("http://pumpk1n.com/lab0.php")
        r = re.findall(r"token=(.*)'", res.text)
        flag = sess.get(f"http://pumpk1n.com/flag.php?token={r[0]}")
        if i == 1336:
            print(flag.text)