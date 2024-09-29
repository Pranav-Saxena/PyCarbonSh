***********
PyCarbonSh 
***********

.. image:: pycarbonsh.png
    :align: center
    :target: https://github.com/Pranav-Saxena/PyCarbonSh/
    :alt: PyCarbonSh

*The Asynchronous web-scraper for carbon.now.sh which helps to create and share beautiful pics of your code!*

.. image:: https://discord.com/api/guilds/833364768076988458/embed.png
   :target: https://discord.gg/tTr6DvyRCH
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/pycarbonsh.svg
   :target: https://pypi.python.org/pypi/pycarbonsh
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/pycarbonsh.svg
   :target: https://pypi.python.org/pypi/pycarbonsh
   :alt: PyPI supported Python versions
.. image:: https://img.shields.io/github/license/Pranav-Saxena/PyCarbonSh?color=2b9348.svg
    :target: LICENSE
.. image:: https://img.shields.io/github/stars/Pranav-Saxena/PyCarbonSh?color=2b9348.svg
    :alt: Stars
.. image:: https://img.shields.io/github/forks/Pranav-Saxena/PyCarbonSh?color=2b9348.svg
    :alt: forks


Documentation
---------------------------
`Official Documentation <https://pycarbonsh.readthedocs.io/en/latest/index.html#>`_.

Support
---------------------------
For support using PyCarbonSh, please join the official `support server
<https://discord.gg/tTr6DvyRCH>`_ on `Discord <https://discordapp.com/>`_.

Installation
---------------------------
The following commands are currently the valid ways of installing PyCarbonSh.

Through pip
############

**Windows**

.. code:: sh

    py -3 -m pip install pycarbonsh

**Linux/MacOS**

.. code:: sh

    python3 -m pip install pycarbonsh


To install master branch
#########################

**Windows**

.. code:: sh

    py -3 -m pip install -U git+https://github.com/Pranav-Saxena/PyCarbonSh@master

**Linux/MacOS**

.. code:: sh

    python3 -m pip install -U git+https://github.com/Pranav-Saxena/PyCarbonSh@master

Manual Installation
####################
    .. note:: Ensure that an up-to-date version of setuptools is installed. ``python -m pip install --upgrade setuptools``

- ``git clone https://github.com/Pranav-Saxena/PyCarbonSh/``
- ``cd PyCarbonSh``
- ``python3 setup.py install`` 

    .. note:: Use ``sudo python3 setup.py install`` on linux if some error pops up

Usage
#######
    .. note:: When you run pycarbonsh for the first time, it downloads the latest version of Chromium (~150MB) if it is not found on your system. If you don't prefer this behavior, ensure that a suitable Chrome binary is installed. One way to do this is to run ``pyppeteer-install`` command before prior to using this library.

Getting Started
----------------------------

A quick and easy example to get started with PyCarbonSh

.. code:: py

    from pycarbonsh import generatecarbon
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generatecarbon(code="Made with ❤ by Pranav Saxena"))


Support Me
-----------
Support Me by adding my bot to your server :) `Invite Inferno Here <https://discord.com/api/oauth2/authorize?client_id=808690602358079508&permissions=261926419703&scope=bot%20applications.commands>`_

Contribute
----------------------------
Any contributions you make are **greatly appreciated**.
    
- PRs are accepted!!
- If you have some ideas for new features and you don't have time to implement them please open an issue with the tag new_feature.
- Please don't forget to comment (document) your code!
