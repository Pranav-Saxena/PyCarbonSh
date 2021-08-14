Welcome to PyCarbonSh's Documentation
======================================
.. image:: /images/pycarbonsh.png

The Asynchronous web-scraper for carbon.now.sh which helps to create and share beautiful pics of your code!
    
**Features:**

- Easy to Use
- It's Asynchronous so won't block your code execution
- Lots of options for customization
    
Support
---------

If you're having trouble with something, these resources might help.

- Ask us and hang out with us in our `Support Server <http://discord.gg/tTr6DvyRCH>`_ on `Discord <https://discordapp.com/>`_ .
- Report bugs in the `issue tracker <https://github.com/Pranav-Saxena/PyCarbonSh/issues>`_.
- Ask in our `GitHub discussions page <https://github.com/Pranav-Saxena/PyCarbonSh/discussions/>`_.
    
Installation
---------------
The following commands are currently the valid ways of installing PyCarbonSh.

Through pip
~~~~~~~~~~~~~

**Windows**

.. code:: sh

    py -3 -m pip install pycarbonsh

**Linux/MacOS**

.. code:: sh

    python3 -m pip3 install pycarbonsh
To install master branch
~~~~~~~~~~~~~~~~~~~~~~~~~
**Windows**

.. code:: sh

    py -3 -m pip install -U git+https://github.com/Pranav-Saxena/PyCarbonSh@master

**Linux/MacOS**

.. code:: sh

    python3 -m pip3 install -U git+https://github.com/Pranav-Saxena/PyCarbonSh@master

Manual Installation
~~~~~~~~~~~~~~~~~~~
- ``git clone https://github.com/Pranav-Saxena/PyCarbonSh/``
- ``setup.bat``
- ``venv\scripts\activate``
- ``pycarbonsh``

Usage
~~~~~~~
.. note:: When you run pycarbonsh for the first time, it downloads the latest version of Chromium (~150MB) if it is not found on your system. If you don't prefer this behavior, ensure that a suitable Chrome binary is installed. One way to do this is to run ``pyppeteer-install`` command before prior to using this library.


Getting Started
----------------------------
    
A quick and easy example to get started with PyCarbonSh
    
.. code:: py
    
    from pycarbonsh import generatecarbon
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generatecarbon(code="Made with ❤ by Pranav Saxena"))    


Parameters
------------
The parameters available for customization are listed below!!

path
~~~~~
Required(str)

The Location where the filed will be saved (don't add filename to it)

Example

.. code:: py

   C:/Users/Pranav/Desktop
    
code
~~~~~
optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_ ) --> Defaults to "Made with ❤ by Pranav Saxena"

The code for whose image you want to generate.

bg
~~~~
optional( `str <https://docs.python.org/3/library/stdtypes.html#str>`_ ) --> Defaults to "rgba(74, 144, 226, 100)"

The background colour of the image. 
    
Should be of the format "rgba(<number>,<number>,<number>,<number>)" or "#<hexcode>"

fontSize
~~~~~~~~~~~~~~~
Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to "14px"

The Font Size of code in the image 
Should be of the format "<fontsize>px"

fontfamily
~~~~~~~~~~~
Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to "Hack" fontfamily

The Font Family for code in the image
Get List of Available FontFamilies `Here <addlink>`

theme
~~~~~~
Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to "seti" theme

Theme of the Image
Get List of Available Themes `Here <addlink>`

exportsize
~~~~~~~~~~~~~
    Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) -->Defaults to "2x"

    The size of Image to be saved

    Should be in ["1x","2x","4x"]

language
~~~~~~~~~
    Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to "auto"

    The Programming Language of the code in the image.

    Get List of Available Languages `Here <addlink>`

widthAdjustment
~~~~~~~~~~~~~~~~
    Optional(`bool <https://docs.python.org/3/library/functions.html#bool>`_) --> Defaults to True
    
    Parameter to enable/disable autowithadjustment of image according to size of the code.

linenumbers
~~~~~~~~~~~~~~~~
    Optional(`bool <https://docs.python.org/3/library/functions.html#bool>`_) --> Defaults to False
    
    Parameter to enable/disable linenumbers for code in the image

firstlinenumber
~~~~~~~~~~~~~~~~
    Optional(`int <https://docs.python.org/3/library/functions.html#int>`_) --> Defaults to 1

    The number from which line numbers should start if linenumbers are enabled
    
lineheight
~~~~~~~~~~~~~~~~~~
    Optional(`int <https://docs.python.org/3/library/functions.html#int>`_) --> Defaults to 130

    Spacing between lines

paddingvertical
~~~~~~~~~~~~~~~~
    Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to "56px"

    Should be of the format "<number>px"

    Space between borders and the code (for top and bottom)

paddingHorizontal
~~~~~~~~~~~~~~~~~~
    Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to "56px"

    Should be of the format "<number>px"

    Space between borders and the code (for left and right)

squaredImage
~~~~~~~~~~~~~
    Optional(`bool <https://docs.python.org/3/library/functions.html#bool>`_) --> Defaults to False

    Enable/disable to get perfect square borders (Defaults to Rounded)

watermark
~~~~~~~~~~~~~
    Optional(`bool <https://docs.python.org/3/library/functions.html#bool>`_) --> Defaults to False

    Enable/Disable watermark of `Carbon <https://carbon.now.sh/>_`

dropShadow
~~~~~~~~~~~~~
    Optional(`bool <https://docs.python.org/3/library/functions.html#bool>`_) --> Defaults to True

    Enable/Disable shadow

dropShadowBlurRadius
~~~~~~~~~~~~~~~~~~~~~~
    Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to "68px"

    Shadow Blur Radius

    Should be of the format "<number>px"

dropShadowOffsetY
~~~~~~~~~~~~~~~~~~
    Optionalstr() --> Defaults to "20px"

    Shadow Offset Y

    Should be of the format "<number>px"

windowControls
~~~~~~~~~~~~~~~~
    Optional(`bool <https://docs.python.org/3/library/functions.html#bool>`_) --> Defaults to True

    Enable/Disable Window Controls

windowTheme
~~~~~~~~~~~~~
    Optional(`str <https://docs.python.org/3/library/stdtypes.html#str>`_) --> Defaults to None

    Window Theme For the Image

    Get List of Available Window Themes `Here`


Available Options For Few Parameters
-------------------------------------

Font Family
~~~~~~~~~~~~
Here is the List of Available Font Families!!
    

Themes
~~~~~~~~~
Here is the list of Available Themes!
    
.. csv-table:: 
   :file: /datafiles/themesn.csv
   :header-rows: 1

   
Languages
~~~~~~~~~
You Can You use any programming language in parameters (full name)

and the accepted aliases of the languages are mentioned below:
     

.. csv-table:: 
   :file: /datafiles/langs.csv
   :width: 5,5
   :header-rows: 1



Window Themes
~~~~~~~~~~~~~~
Here is the list of available Window Themes
    
- none
- sharp
- bw
- boxy

License
---------
MIT License

Copyright (c) 2021 PRANAV SAXENA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

