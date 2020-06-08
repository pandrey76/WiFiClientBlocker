#!/bin/bash

base_work_folder=""
base_python_interpreter=""
# shellcheck disable=SC2162
read -p "Please, enter working folder name: " base_work_folder

# Идём в рабочий каталог пользователя
cd ~
echo "User folder:  $(pwd)"

# Создаём рабочую директорию
mkdir "$base_work_folder"

cd "$base_work_folder"
# shellcheck disable=SC2005
echo "Current folder:  $(pwd)"

sudo apt update

# Install git
sudo apt install git


# sudo apt install python3-dev, python3-venv, python3-tk

# Install Python development tools
sudo apt install python3-dev

# Install Python virtual environment
sudo  apt install python3-venv

# Install Python virtual environment
sudo  apt install python3-tk

# Install JSON quire
sudo  apt install jq

sudo apt update

git clone "https://github.com/pandrey76/WiFiClientBlocker.git"

# shellcheck disable=SC2162
read -p "Python interpreter: " base_python_interpreter

cd "WiFiClientBlocker"

echo "Current folder:  $(pwd)"

$base_python_interpreter -m venv venv

. venv/bin/activate

pip3 install -U pip
pip3 install -r requirements.txt

# pip3 install --ignore-installed -r requirements.txt


#GECKO_DRIVER_INSTALL_DIR=$(pwd)
#url=""
#architect=$(uname --m)
#SUB="64"
## shellcheck disable=SC1069
#if["$architect" =~ .*"$SUB".*]
#  then
#  url=$(curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
#  architect = "x64"
#else
#  url=$(curl -s 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | jq -r '.assets[].browser_download_url | select(contains("linux32"))')
#  architect = "x32"
#fi
#  echo "Current machine architect type is $architect"
#
#curl -s -L "$url" | tar -xz

#
#echo "url2"
#echo "$url2"
#
## Не работает
##echo "$HOSTTYPE"
##echo "$OSTYPE"
#
#echo "$HOME"
#
##curl -s -L "$url2" | tar -xz
##chmod +x geckodriver
##sudo mv geckodriver "$INSTALL_DIR"
#echo "installed geckodriver binary in $INSTALL_DIR"
###

## Возвращаем информацию об последней версией
#json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
#
#url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
#
#curl -s -L "$url" | tar -xz
#chmod +x geckodriver
#sudo mv geckodriver "$INSTALL_DIR"
#echo "installed geckodriver binary in $INSTALL_DIR"



#project_path=$(pwd) + base_work_folder
#echo "$project_path"

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


## Getting curent user
#echo "$USER"
# or
#whoami
#
## What the os version type
#cat proc/version
#> Linux version 4.19.0-9-amd64 (debian-kernel@lists.debian.org) (gcc version 8.3.0 (Debian 8.3.0-6)) #1 SMP Debian 4.19.118-2 (2020-04-29)
#
##admin1@ubuntu18:/$ cat /etc/os-release
##    NAME="Ubuntu"
##    VERSION="18.04.4 LTS (Bionic Beaver)"
##    ID=ubuntu
##    ID_LIKE=debian
##    PRETTY_NAME="Ubuntu 18.04.4 LTS"
##    VERSION_ID="18.04"
##    HOME_URL="https://www.ubuntu.com/"
##    SUPPORT_URL="https://help.ubuntu.com/"
##    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
##    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
##    VERSION_CODENAME=bionic
##    UBUNTU_CODENAME=bionic
#
##admin1@ubuntu18:/$ lsb_release -a
##    No LSB modules are available.
##    Distributor ID:	Ubuntu
##    Description:	Ubuntu 18.04.4 LTS
##    Release:	18.04
##    Codename:	bionic
##
##admin1@ubuntu18:/$ hostnamectl
##    Static hostname: ubuntu18
##    Icon name: computer-desktop
##    Chassis: desktop
##    Machine ID: 40ac2e4867354807898b27dac3d6375c
##    Boot ID: 6c9d1b71f35843d8879e18f02d58e42d
##    Operating System: Ubuntu 18.04.4 LTS
##    Kernel: Linux 4.15.0-99-generic
##    Architecture: x86-64
##
##admin1@ubuntu18:/$ uname -r
##    4.15.0-99-generic
##
##admin1@ubuntu18:/$ cat /etc/issue
##    Ubuntu 18.04.4 LTS \n \l
#
##admin1@ubuntu18:/$ uname --m
#    #x86_64
#
##admin1@ubuntu18:/$ uname -i
##    x86_64
#
#
## Installing FireFox
#sudo apt update
#sudo apt install firefox-esr
#sudo apt update
#firefox -v
#
## Installing latest version of geckodriver for Selenium
## One way not automatic
#Here are the steps:
#
#    Go to the geckodriver releases page. Find the latest version of the driver for your platform and download it. For example:
#
#        wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
#        # wget "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz"
#
#    Extract the file with:
#
#        tar -xvzf geckodriver*
#
#    Make it executable:
#
#        chmod +x geckodriver
#
#    Add the driver to your PATH so other tools can find it:
#
#        export PATH=$PATH:/path-to-extracted-file/.
#
#        # sudo cp /home/pi/Downloads/geckodriver /usr/local/bin/geckodriver
#
#
## Way Two
## Getting latest version full automatic
## Need to see more carefully
#####
## Устанавливаем JSON query
#sudo apt install jq
#
#INSTALL_DIR="/usr/local/bin"
## Возвращаем информацию об последней версией
#json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
#
#url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
#
#curl -s -L "$url" | tar -xz
#chmod +x geckodriver
#sudo mv geckodriver "$INSTALL_DIR"
#echo "installed geckodriver binary in $INSTALL_DIR"
####
#
## Editing Raspbean LXDE Desktop autostart file.
## Running python script in user mode.
#    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
#
#        @lxpanel --profile LXDE-pi
#        @pcmanfm --desktop --profile LXDE-pi
#
#        @lxterminal
#        @lxterminal -e /usr/bin/python3
#        @lxterminal -e /home/pi/work/WiFiClientBlocker/venv/bin/python3
#
#        @/home/pi/work/WiFiClientBlocker/venv/bin/python3 /home/pi/work/WiFiClientBlocker/ShedulerScriptRun.py
#
#        #Work to
#        #@/usr/bin/python3 /home/pi/work/WiFiClientBlocker/SchedulerScriptRun.py
#
#        @xscreensaver -no-splash
#
## Metod 2 (Not work)
#    sudo nano ~/.config/lxsession/LXDE/autostart
#
#
#
#
#
