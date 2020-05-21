#!/bin/bash

echo "Beginning execution run.sh shell script."

# Запуск скрипта python из через crontab
# python3 /home/admin1/work/WiFiClientBlocker/RoutersInspector.py

# Запуск скрипта python из venv через crontab
# Вариант №1
/home/admin1/work/WiFiClientBlocker/venv/bin/python3 "/home/admin1/work/WiFiClientBlocker/RoutersInspector.py"

# Вариант №2
# cd "/home/admin1/work/WiFiClientBlocker"
# venv/bin/python3 "RoutersInspector.py"

# python3 "RoutersInspector.py"

echo "Ended execution run.sh shell script."

# exit

