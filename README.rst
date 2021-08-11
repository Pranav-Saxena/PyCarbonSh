***********
PyCarbonSh 
***********

.. image:: https://cdn.discordapp.com/attachments/862939982837317672/875030619606888458/pycarbonsh.png
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

    pip install pycarbonsh

**Linux/MacOS**

.. code:: sh

    pip3 install pycarbonsh

Manual Installation
####################
- ``git clone https://github.com/Pranav-Saxena/PyCarbonSh/``
- ``setup.bat``
- ``venv\scripts\activate``
- ``pycarbonsh``

Getting Started
----------------------------

A quick and easy example to get started with PyCarbonSh

.. code:: py

    from pycarbonsh import generatecarbon
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generatecarbon(code="Made with ❤ by Pranav Saxena"))

Contribute
----------------------------
Any contributions you make are **greatly appreciated**.
    
- PRs are accepted!!
- If you have some ideas for new features and you don't have time to implement them please open an issue with the tag new_feature.
- Please don't forget to comment (document) your code!