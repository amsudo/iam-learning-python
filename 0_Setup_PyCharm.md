Setup PyCharm
=============

*By Charles Hii @ 2018-08-24*


### Python 3

1. Ubuntu 18.04 came with Python 3 pre-installed.

        $ python3 -V
        Python 3.6.5


2. PyCharm required python3-distutils

        $ sudo apt-get install python3-distutils


### PyCharm

1. Setup python intepreter.

        - On the [ Welcome to PyCharm ] dialog, select [ Configure > Setting ]
        - On the [Settings for New Projects ] dialog, select [ Project Interpreter ]
        - Click on [ Gear button > Add ] to open [ Add Python Interpreter ] dialog
        - Select Virtualenv Environment
            - Location : /root
            - Base intepreter : /usr/bin/python3.6
            - Inherit global site-packages : Checked
            - Make available to all projects : Checked
            - Click OK button
        - Click OK button


2. Create New Project

        - Pure Python
        - Location : /root/PycharmProjects/MyFirstProject
        - Click Create button








