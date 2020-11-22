#!/usr/bin/bash

# Load the main functions
source "functions.sh"


# this function checks whats needed for shell script
function check_requirments {
    if ! [[ "$(python3 -V)" =~ "Python 3" ]]; then
        install_python
    else
        echo "> Python3 status : OK"
    fi
    if ! [[ "$(pip3 --version)" =~ "pip 1" ]]; then
        install_pip
    else
        echo "> Pip3 status : OK"
    fi
    if ! [[ "$(python3 -h venv)" =~ "usage: python3" ]]; then
        install_venv
    else
        echo "> Venv status : OK"
    fi
    if ! [[ "$(unzip -v)" =~ "UnZip" ]]; then
        set_unzip
    else
        echo "> Unzip status : OK"
    fi
    echo "Requirements checked."
}


echo "Running installer ..."
check_requirments
echo "Exit staus : 0"
