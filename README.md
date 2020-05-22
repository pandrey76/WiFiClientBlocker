# WiFiClientBlocker
Blocking Wi-Fi clients through the blacklisting mechanism of the router.


# Run the script through crontab (Linux version).

In order to edit the crontab file, you need to enter the command in the terminal

    'crontab -e '

The crontab file will open

The instructions for cron are in the format

    minute hour day month day_week /path/to/executable/file

Let's look at an example: we’ll set it to start automatically every minute, for this we will write the instruction 
in crontab. Run script by crontab:

    */1 * * * * /root/environments/my_env/bin/python /root/environments/my_env/parser_hh.py

Let's understand what each part of the instruction means.

    */1 * * * *
    
here we say that we want to run the script every minute, every hour, every day, every month
/root/environments/my_env/bin/python

My script is in a virtual environment, so you need to point out that you need to run Python in a virtual environment,
for this we write the path to python /root/environments/my_env/parser_hh.py.

Specify the path to the executable file, in our case, the file parser_hh.py

As a result, our instruction means the following. We tell cron that we want to run the parser_hh.py file from 
the my_env virtual environment every minute.


Important

Before setting up a file launch. You need to make sure that the file has execute access, otherwise your script 
will not be launched. If your server has an isp manager control panel, you can configure cron using it. 
Find the scheduler link, in fact it is the same crown, only in the graphical interface. 
To allow the script to run, use the following command.

    chmod -x file

Now in accordance with the above add instructions to crontab.

Important.

When editing a file, you must leave an empty line at the end. Otherwise, the file will not be saved.

Run terminal:

    chmod -x "RoutersInspector.py"

    crontab -e

Editing crontab setting file: 
       
    */2 * * * * /home/admin1/work/WiFiClientBlocker/venv/bin/python3 /home/admin1/work/WiFiClientBlocker/RoutersInspector.py

    Type "Enter" for insert New string symbol fnd save.
    
If we wont to see crontab log, so we must execute next command:
    
    grep CRON /var/log/syslog
    
Now work ok, bun python script inside bush script don't starting.

    */1 * * * * sh /home/admin1/work/WiFiClientBlocker/run.sh >> /home/admin1/cron_run_sh.log    

Варианты запуска скриптов из crontab через каждую минуту:

    */1 * * * * python3 /home/admin1/work/WiFiClientBlocker/hello_crontab.py >> hello_crontab.log
    */1 * * * * python3 /home/admin1/work/WiFiClientBlocker/RoutersInspector.py >> RoutersInspector.log
    */1 * * * * /home/admin1/work/WiFiClientBlocker/venv/bin/python3 "/home/admin1/work/WiFiClientBlocker/RoutersInspector.py" >> RoutersInspector_from_venv.log

К сожалению через crontab не удалось запускать браузер, так что данный сервис под наш проект мы использовать не будем.



pi@raspberry:~ $ sudo nano /etc/xdg/lxsession/LXDE-pi/autostart


@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi

#@lxterminal
#@bash -c sleep 5
#@/usr/bin/python3 /home/pi/work/WiFiClientBlocker/RoutersInspector.py >> /home$
#@lxterminal 
#@sh -c 'sleep 10'
#@/usr/bin/python3 "/home/pi/work/WiFiClientBlocker/RoutersInspector.py"
#@lxterminal
#@sh -c sleep 10

@/usr/bin/python3 /home/pi/work/WiFiClientBlocker/RoutersInspector.py
@lxterminal
#@lxterminal -e '/usr/bin/python3 /home/pi/work/WiFiClientBlocker/RoutersInspect$
#@lxterminal -e "/usr/bin/python3 /home/pi/work/WiFiClientBlocker/RoutersInspect$
#@lxterminal -e /usr/bin/python3 /home/pi/work/WiFiClientBlocker/RoutersInspecto$
@/usr/bin/python3 /home/pi/work/WiFiClientBlocker/SchedulerScriptRun.py

@xscreensaver -no-splash



