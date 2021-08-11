
.. currentmodule:: PyCarbonSh

    Welcome to PyCarbonSh's Documentation
    ======================================
    .. image:: /images/pycarbonsh.png
    The Asynchronous web-scraper for carbon.now.sh which helps to create and share beautiful pics of your code!
    

    
    **Features:**
    - Easy to Use
    - It's Asynchronous so won't block your code execution
    - Lots of options for customization
    
    Support
    --------------
    
    If you're having trouble with something, these resources might help.
    - Ask us and hang out with us in our `Support Server<http://discord.gg/tTr6DvyRCH>` on `Discord <https://discordapp.com/>`.
    - If you're looking for something specific, try the :ref:`index <genindex>` or :ref:`searching <search>`.
    - Report bugs in the `issue tracker <https://github.com/Pranav-Saxena/PyCarbonSh/issues>`.
    - Ask in our `GitHub discussions page <https://github.com/Pranav-Saxena/PyCarbonSh/discussions/>`.
    
    Installation
    ---------------
    The following commands are currently the valid ways of installing PyCarbonSh.

    Through pip
    ########

    **Windows**

    .. code:: sh

        pip install pycarbonsh

    **Linux/MacOS**

    .. code:: sh

        pip3 install pycarbonsh

    Manual Installation
    ########
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


    Parameters
    ------------
    The parameters available for customization are listed below!!

    path
    ~~~~~
    Required(str)

    The Location where the filed will be saved (don't add filename to it)

    Example:
    .. code::
        C:/Users/Pranav/Desktop
    
    code
    ~~~~~
    optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "Made with ❤ by Pranav Saxena"

    The code for whose image you want to generate.

    bg
    ~~~~
    optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "rgba(74, 144, 226, 100)"

    The background colour of the image. 
    
    Should be of the format "rgba(<number>,<number>,<number>,<number>)" or "#<hexcode>"

    fontSize
    ~~~~~~~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "14px"

    The Font Size of code in the image 

    Should be of the format "<fontsize>px"

    fontfamily
    ~~~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "Hack" fontfamily

    The Font Family for code in the image

    Get List of Available FontFamilies `Here <addlink>`

    theme
    ~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "seti" theme

    Theme of the Image

    Get List of Available Themes `Here <addlink>`

    exportsize
    ~~~~~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) -->Defaults to "2x"

    The size of Image to be saved

    Should be in ["1x","2x","4x"]

    language
    ~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "auto"

    The Programming Language of the code in the image.

    Get List of Available Languages `Here <addlink>`

    widthAdjustment
    ~~~~~~~~~~~~~~~~
    Optional(`bool<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to True
    
    Parameter to enable/disable autowithadjustment of image according to size of the code.

    linenumbers
    ~~~~~~~~~~~~~~~~
    Optional(`bool<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to False
    
    Parameter to enable/disable linenumbers for code in the image

    firstlinenumber
    ~~~~~~~~~~~~~~~~
    Optional(`int<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to 1

    The number from which line numbers should start if linenumbers are enabled
    
    lineheight
    ~~~~~~~~~~~~~~~~~~
    Optional(`int<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to 130

    Spacing between lines

    paddingvertical
    ~~~~~~~~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "56px"

    Should be of the format "<number>px"

    Space between borders and the code (for top and bottom)

    paddingHorizontal
    ~~~~~~~~~~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "56px"

    Should be of the format "<number>px"

    Space between borders and the code (for left and right)

    squaredImage
    ~~~~~~~~~~~~~
    Optional(`bool<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to False

    Enable/disable to get perfect square borders (Defaults to Rounded)

    watermark
    ~~~~~~~~~~~~~
    Optional(`bool<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to False

    Enable/Disable watermark of `Carbon`

    dropShadow
    ~~~~~~~~~~~~~
    Optional(`bool<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to True

    Enable/Disable shadow

    dropShadowBlurRadius
    ~~~~~~~~~~~~~~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to "68px"

    Shadow Blur Radius

    Should be of the format "<number>px"

    dropShadowOffsetY
    ~~~~~~~~~~~~~~~~~~
    Optionalstr() --> Defaults to "20px"

    Shadow Offset Y

    Should be of the format "<number>px"

    windowControls
    ~~~~~~~~~~~~~~~~
    Optional(`bool<https://docs.python.org/3/library/functions.html#int>`) --> Defaults to True

    Enable/Disable Window Controls

    windowTheme
    ~~~~~~~~~~~~~
    Optional(`str<https://docs.python.org/3/library/stdtypes.html#str>`) --> Defaults to None

    Window Theme For the Image

    Get List of Available Window Themes `Here`


    Available Options For Few Parameters
    -------------------------------------

    Font Family
    ~~~~~~~~~~~~
    Here is the List of Available Font Families!!
    
    Font Family Name to be written          Actual Font Family
    in the parameter while calling 
    the function

    -MonoLisa                                MonoLisa
    -dm                                      Dank Mono
    -Anonymous+Pro                           Anonymous Pro
    -Droid+Sans+Mono                         Droid Sans Mono
    -Fantasque+Sans+Mono                     Fantasque Sans Mono
    -Fira+Code                               Fira Code
    -Hack                                    Hack
    -IBM+Plex+Mono                           IBM Plex Mono
    -Inconsolata                             Inconsolata
    -Iosevka                                 Iosevka
    -JetBrains+Mono                          JetBrains Mono
    -Monoid                                  Monoid
    -Source+Code+Pro                         Source Code Pro
    -Space+Mono                              Space Mono
    -Ubuntu+Mono                             Ubuntu Mono

    Themes
    ~~~~~~~~~
    Here is the list of Available Themes!
    
    -3024-night
    -a11y-dark
    -blackboard
    -base16-dark
    -base16-light
    -cobalt
    -dracula-pro
    -duotone-dark
    -hopscotch
    -lucario
    -material
    -monokai
    -night-owl
    -nord
    -oceanic-next
    -one-light
    -one-dark
    -panda-syntax (panda)
    -paraiso-dark
    -seti
    -shades-of-purple
    -solarized+dark
    -solarized+light
    -synthwave-84
    -twilight
    -verminal
    -vscode
    -yeti
    -zenburn


    
    Languages
    ~~~~~~~~~
    You Can You use any programming language in parameters (full name)

    and the accepted aliases of the languages are mentioned below:
     
     Alias          Language
    -htaccess       apache
    -sh             bash
    -c              c
    -h              c
    -C              c++
    -cc             c++
    -cpp            c++
    -cxx            c++
    -c++            c++
    -hh             c++
    -hpp            c++
    -hxx            c++
    -h++            c++
    -cs             csharp
    -clj            clojure
    -cljs           clojure
    -cljc           clojure
    -edn            clojure
    -cbl            cobol
    -cob            cobol
    -cpy            cobol
    -coffee         coffeescript
    -litcoffee      coffeescript
    -cr             crystal
    -css            css
    -d              d
    -dart           dart
    -ex             elixir
    -exs            elixir
    -erl            erlang
    -hrl            erlang
    -f              fortran
    -for            fortran
    -f90            fortran
    -fs             mllike
    -fsi            mllike
    -fsx            mllike
    -fsscript       mllike
    -ml             mllike
    -mli            mllike
    -graphql        graphql
    -gql            graphql
    -go             golang
    -groovy         groovy
    -hbs            handlebars
    -handlebars     handlebars
    -hs             haskell
    -lhs            haskell
    -hx             haxe
    -hxml           haxe
    -html           htmlmixed
    -java           java
    -class          java
    -jar            java
    -js             javascript
    -json           json
    -jsx            jsx
    -kt             kotlin
    -kts            kotlin
    -tex            stex
    -lisp           commonlisp
    -cl             commonlisp
    -lsp            commonlisp
    -md             markdown
    -nb             mathematica
    -wl             mathematica
    -nt             ntriples
    -conf           nginx
    -nim            nimrod
    -m              objectivec
    -mm             objectivec
    -M              objectivec
    -pp             pascal
    -pas            pascal
    -inc            pascal
    -php            php
    -phtml          php
    -php3           php
    -php4           php
    -php5           php
    -php7           php
    -phps           php
    -php-s          php
    -ps1            powershell
    -ps1xml         powershell
    -psc1           powershell
    -psd1           powershell
    -psm1           powershell
    -pssc           powershell
    -cdxml          powershell
    -py             python
    -pyc            python
    -pyd            python
    -pyo            python
    -pyw            python
    -pyz            python
    -r              r
    -R              r
    -RData          r
    -rds            r
    -rda            r
    -rb             ruby
    -rs             rust
    -rslib          rust
    -sass           sass
    -scss           sass
    -scala          scala
    -sc             scala
    -sql            sql
    -stylus         stylus
    -swift          swift
    -tcl            tcl
    -tbc            tcl
    -toml           toml
    -ttl            turtle
    -ts             typescript
    -tsx            typescript
    -vb             vb
    -v              verilog
    -vhdl           vhdl
    -vhd            vhdl
    -vue            vue
    -xml            xml
    -yaml           yaml
    -yml            yaml



    Window Themes
    ~~~~~~~~~~~~~~
    Here is the list of available Window Themes
    
    -none
    -sharp
    -bw
    -boxy

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



    