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

