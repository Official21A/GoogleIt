#!/usr/bin/bash

# this function installs python3
function install_python {
    sudo apt-get update
    sudo apt-get install python3.6
    python3 --version
    echo "Python3 is now installed on your system."
}

# this function installs pip3
function install_pip {
    sudo apt-get update
    sudo apt install python3-pip
    pip3 --version
    echo "Pip3 is now installed on your system."
}

# this function installs virtualenv
function install_venv {
    sudo apt-get update
    pip3 install virtualenv
    pip3 freeze | grep virtualenv
    echo "Virualenv is now installed on your python3."
}

# this function installs the upzip command
function set_unzip {
    sudo apt install unzip
    unzip -v
    echo "Unzip is now installed on your system."
}
