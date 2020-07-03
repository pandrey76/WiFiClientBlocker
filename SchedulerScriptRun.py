import schedule
import os
import traceback
import datetime
from time import sleep
# from RoutersInspector import RoutersInspector
from IRemoteManager import IRemoteManager


def job():
    # os.system( "/home/admin1/work/WiFiClientBlocker/venv/bin/python3
    # /home/admin1/work/WiFiClientBlocker/RoutersInspector.py")

    # obj = RoutersInspector()
    # obj.turn_off()
    try:
        remote_manager = IRemoteManager()
        remote_manager.process()
    except Exception as er:
        with open("scheduler_err.log", 'a') as g:
            separate = "************************"
            space = ' '
            result_str = separate + space + str(datetime.datetime.now()) + space + separate
            result_str += os.linesep
            result_str += traceback.format_exc()
            result_str += os.linesep
            result_str += separate
            result_str += separate
            result_str += separate
            g.write(result_str)
            g.write(os.linesep)


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    # sleep(1)
