import schedule
import os
from time import sleep


def job():
    os.system(
        "/home/admin1/work/WiFiClientBlocker/venv/bin/python3 /home/admin1/work/WiFiClientBlocker/RoutersInspector.py")


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    sleep(1)

