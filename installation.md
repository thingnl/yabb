# Installation #

Installation of yabb should be a pretty painless process. Yabb was developed on a Debian Release 7.0 (wheezy) 64-bit, Kernel Linux 3.2.0-4-amd64, GNOME 3.4.2 system.

You will need the following:

- git
- python 2.7.3
- python module python-requests
 


To check your python version use the following command:

- python -V

output should read something like: 

- Python 2.7.3


To install needed software use:

- sudo apt-get install git
- sudo apt-get install python-requests
- sudo git clone https://github.com/thingnl/yabb.git


To configure yabb use:

- cd yabb
- gedit/vi/nano config.py
- **Double check all settings!**

Start your first run:

- python yabb.py or ./yabb.sh

The BTC-e api file key_file is written and you will need to restart YABB.


Start your first actual run:

- python yabb.py or ./yabb.sh

Depending on your settings, you should be up and running doing actual trading or just simulations.



