#!/bin/bash
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
# Need to see more smily
#### 
INSTALL_DIR="/usr/local/bin"

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
    




