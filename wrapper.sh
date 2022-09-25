#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi
if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'Error: 
    it looks like pip3 is not installed.
    To install pip3, check out https://pypi.org/project/pip/' >&2
  exit 1
fi

pip3 install -r requirements.txt 
python3 main.py