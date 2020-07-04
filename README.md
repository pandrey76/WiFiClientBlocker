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




#base_python_interpreter=""
#project_domain=""
#project_path=`pwd`
#
#read -p "Python interpreter: " base_python_interpreter
#read -p "Your domain without protocol (for example, google.com): " project_domain
#`$base_python_interpreter -m venv env`
#source env/bin/activate
#pip install -U pip
#pip install -r requirements.txt
#
#sed -i "s~dbms_template_path~$project_path~g" nginx/site.conf systemd/gunicorn.service
#sed -i "s~dbms_template_domain~$project_domain~g" nginx/site.conf src/config/settings.py
#
#sudo ln -s $project_path/nginx/site.conf /etc/nginx/sites-enabled/
#sudo ln -s $project_path/systemd/gunicorn.service /etc/systemd/system/
#
#sudo systemctl daemon-reload
#sudo systemctl start gunicorn
#sudo systemctl enable gunicorn
#sudo service nginx restart


# Getting curent user
echo "$USER"
 or
whoami

# What the os version type
cat proc/version
> Linux version 4.19.0-9-amd64 (debian-kernel@lists.debian.org) (gcc version 8.3.0 (Debian 8.3.0-6)) #1 SMP Debian 4.19.118-2 (2020-04-29)

#admin1@ubuntu18:/$ cat /etc/os-release
#    NAME="Ubuntu"
#    VERSION="18.04.4 LTS (Bionic Beaver)"
#    ID=ubuntu
#    ID_LIKE=debian
#    PRETTY_NAME="Ubuntu 18.04.4 LTS"
#    VERSION_ID="18.04"
#    HOME_URL="https://www.ubuntu.com/"
#    SUPPORT_URL="https://help.ubuntu.com/"
#    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
#    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
#    VERSION_CODENAME=bionic
#    UBUNTU_CODENAME=bionic

#admin1@ubuntu18:/$ lsb_release -a
#    No LSB modules are available.
#    Distributor ID:	Ubuntu
#    Description:	Ubuntu 18.04.4 LTS
#    Release:	18.04
#    Codename:	bionic
#
#admin1@ubuntu18:/$ hostnamectl
#    Static hostname: ubuntu18
#    Icon name: computer-desktop
#    Chassis: desktop
#    Machine ID: 40ac2e4867354807898b27dac3d6375c
#    Boot ID: 6c9d1b71f35843d8879e18f02d58e42d
#    Operating System: Ubuntu 18.04.4 LTS
#    Kernel: Linux 4.15.0-99-generic
#    Architecture: x86-64
#
#admin1@ubuntu18:/$ uname -r
#    4.15.0-99-generic
#
#admin1@ubuntu18:/$ cat /etc/issue
#    Ubuntu 18.04.4 LTS \n \l

#admin1@ubuntu18:/$ uname --m
    #x86_64

#admin1@ubuntu18:/$ uname -i
#    x86_64


# Installing FireFox
sudo apt update
sudo apt install firefox-esr
sudo apt update
firefox -v

# Installing latest version of geckodriver for Selenium 
# One way not automatic
Here are the steps:

    Go to the geckodriver releases page. Find the latest version of the driver for your platform and download it. For example:

        wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
        # wget "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz"        

    Extract the file with:

        tar -xvzf geckodriver*

    Make it executable:

        chmod +x geckodriver

    Add the driver to your PATH so other tools can find it:

        export PATH=$PATH:/path-to-extracted-file/.
        
        # sudo cp /home/pi/Downloads/geckodriver /usr/local/bin/geckodriver 


# Way Two
# Getting latest version full automatic
# Need to see more carefully
####
# Устанавливаем JSON query
sudo apt install jq

INSTALL_DIR="/usr/local/bin"
# Возвращаем информацию об последней версией
json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)

url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')

curl -s -L "$url" | tar -xz
chmod +x geckodriver
sudo mv geckodriver "$INSTALL_DIR"
echo "installed geckodriver binary in $INSTALL_DIR"
###

# Editing Raspbean LXDE Desktop autostart file.
# Running python script in user mode.
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
    
        @lxpanel --profile LXDE-pi
        @pcmanfm --desktop --profile LXDE-pi

        @lxterminal
        @lxterminal -e /usr/bin/python3
        @lxterminal -e /home/pi/work/WiFiClientBlocker/venv/bin/python3

        @/home/pi/work/WiFiClientBlocker/venv/bin/python3 /home/pi/work/WiFiClientBlocker/ShedulerScriptRun.py
        
        #Work to
        #@/usr/bin/python3 /home/pi/work/WiFiClientBlocker/SchedulerScriptRun.py

        @xscreensaver -no-splash
    
# Metod 2 (Not work)
    sudo nano ~/.config/lxsession/LXDE/autostart

#admin1@ubuntu18:/$ cat /etc/os-release
#    NAME="Ubuntu"
#    VERSION="18.04.4 LTS (Bionic Beaver)"
#    ID=ubuntu
#    ID_LIKE=debian
#    PRETTY_NAME="Ubuntu 18.04.4 LTS"
#    VERSION_ID="18.04"
#    HOME_URL="https://www.ubuntu.com/"
#    SUPPORT_URL="https://help.ubuntu.com/"
#    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
#    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
#    VERSION_CODENAME=bionic
#    UBUNTU_CODENAME=bionic

#admin1@ubuntu18:/$ lsb_release -a
#    No LSB modules are available.
#    Distributor ID:	Ubuntu
#    Description:	Ubuntu 18.04.4 LTS
#    Release:	18.04
#    Codename:	bionic
#
#admin1@ubuntu18:/$ hostnamectl
#    Static hostname: ubuntu18
#    Icon name: computer-desktop
#    Chassis: desktop
#    Machine ID: 40ac2e4867354807898b27dac3d6375c
#    Boot ID: 6c9d1b71f35843d8879e18f02d58e42d
#    Operating System: Ubuntu 18.04.4 LTS
#    Kernel: Linux 4.15.0-99-generic
#    Architecture: x86-64
#
#admin1@ubuntu18:/$ uname -r
#    4.15.0-99-generic
#
#admin1@ubuntu18:/$ cat /etc/issue
#    Ubuntu 18.04.4 LTS \n \l

#admin1@ubuntu18:/$ uname -i
#    x86_64

####
INSTALL_DIR="/usr/local/bin"
# Возвращаем информацию об последней версией

json=$(curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest')
#echo "$json"
url1=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
echo "url1"
echo "$url1"

url2=$(curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | jq -r '.assets[].browser_download_url | select(contains("linux64"))')

echo "url2"
echo "$url2"

# Не работает
#echo "$HOSTTYPE"
#echo "$OSTYPE"

echo "$HOME"

#curl -s -L "$url2" | tar -xz
#chmod +x geckodriver
#sudo mv geckodriver "$INSTALL_DIR"
echo "installed geckodriver binary in $INSTALL_DIR"
###


echo "Beginning execution run.sh shell script."

# Запуск скрипта python из через crontab
# python3 /home/admin1/work/WiFiClientBlocker/RoutersInspector.py

# Запуск скрипта python из venv через crontab
# Вариант №1
#/home/admin1/work/WiFiClientBlocker/venv/bin/python3 "/home/admin1/work/WiFiClientBlocker/RoutersInspector.py"

# Вариант №2
# cd "/home/admin1/work/WiFiClientBlocker"
# venv/bin/python3 "RoutersInspector.py"

# python3 "RoutersInspector.py"

# Корремктная запись запуска скрипта Python через crontab
# python3 "/home/admin1/work/WiFiClientBlocker/hello_crontab.py" >> "/home/admin1/running_run_sh_file.log"


#admin1@ubuntu18:/$ cat /etc/os-release
#    NAME="Ubuntu"
#    VERSION="18.04.4 LTS (Bionic Beaver)"
#    ID=ubuntu
#    ID_LIKE=debian
#    PRETTY_NAME="Ubuntu 18.04.4 LTS"
#    VERSION_ID="18.04"
#    HOME_URL="https://www.ubuntu.com/"
#    SUPPORT_URL="https://help.ubuntu.com/"
#    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
#    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
#    VERSION_CODENAME=bionic
#    UBUNTU_CODENAME=bionic

#admin1@ubuntu18:/$ lsb_release -a
#    No LSB modules are available.
#    Distributor ID:	Ubuntu
#    Description:	Ubuntu 18.04.4 LTS
#    Release:	18.04
#    Codename:	bionic
#
#admin1@ubuntu18:/$ hostnamectl
#    Static hostname: ubuntu18
#    Icon name: computer-desktop
#    Chassis: desktop
#    Machine ID: 40ac2e4867354807898b27dac3d6375c
#    Boot ID: 6c9d1b71f35843d8879e18f02d58e42d
#    Operating System: Ubuntu 18.04.4 LTS
#    Kernel: Linux 4.15.0-99-generic
#    Architecture: x86-64
#
#admin1@ubuntu18:/$ uname -r
#    4.15.0-99-generic
#
#admin1@ubuntu18:/$ cat /etc/issue
#    Ubuntu 18.04.4 LTS \n \l

#admin1@ubuntu18:/$ uname -i
#    x86_64

####
INSTALL_DIR="/usr/local/bin"
# Возвращаем информацию об последней версией

json=$(curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest')
#echo "$json"
url1=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
echo "url1"
echo "$url1"

url2=$(curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | jq -r '.assets[].browser_download_url | select(contains("linux64"))')

echo "url2"
echo "$url2"

# Не работает
#echo "$HOSTTYPE"
#echo "$OSTYPE"

echo "$HOME"

#curl -s -L "$url2" | tar -xz
#chmod +x geckodriver
#sudo mv geckodriver "$INSTALL_DIR"
echo "installed geckodriver binary in $INSTALL_DIR"
###

echo "Ended execution run.sh shell script."


Sending email msg to gmail.com.

1. Входим в нужный аккаунт Google;
2. Входим в настройки и отключаем двухфакторную аутентификацию если она включена;
3. В поисковике google.ru набить "less secure apps" и переходим по сслке;
4. Включаем параметр "Небезопасные приложения заблокированы" в "Разрешить".

    Этого достаточно, чтобы отправлять и получать сообщения с акаунта goole через программную реализацию
написанную, например,  на Python. 

    Далее если нам необходимо определить отдельный пароль для конкрнтной программной реализации для доступа
к аккаунту google, то мы делаем следующее:

1. Под нужным аккаунтом в поисковике google.ru печатаем "App passwords" и переходим по ссылке;
2. Попадаем во вкладку Пароли приложений и получаем "Эта настройка недоступна для вашего аккаунта".
    Причин может быть две:
        - не включена двухфакторная авторизация (FA) для аккаунта;
        - у Вас корпоративный аккаунт.
        
2020.07.04 
    Фиксация первой работающей версии для роутера 'Huawei_R100_1'.
        Необходимо создать два шаблона в своём почтовом ящике:
            Для обоих шаблонов адреса и темы должны совпадать:
                - Адрес почтового ящика, определённого первым в списке "remote_sources"
                в файле "RemoteSources.json";
                - Тема "RouTer".
            Тело сообщения (письма) должно различаться и иметь следующее содержание:
                - Блокировка роутера:
                    {"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }
                - Разблокировка роутера:
                    {"action": "recover_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }

                  