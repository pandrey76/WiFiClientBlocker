import schedule
import os
from time import sleep
from RoutersInspector import RoutersInspector


def job():
    # os.system( "/home/admin1/work/WiFiClientBlocker/venv/bin/python3
    # /home/admin1/work/WiFiClientBlocker/RoutersInspector.py")

    obj = RoutersInspector()
    obj.turn_off()


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    # sleep(1)
