import schedule
import os
from time import sleep
# from RoutersInspector import RoutersInspector
from IRemoteManager import IRemoteManager


def job():
    # os.system( "/home/admin1/work/WiFiClientBlocker/venv/bin/python3
    # /home/admin1/work/WiFiClientBlocker/RoutersInspector.py")

    # obj = RoutersInspector()
    # obj.turn_off()

    remote_manager = IRemoteManager()
    remote_manager.process()


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    # sleep(1)
