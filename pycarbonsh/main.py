import asyncio
import os
from pyppeteer import launch
from typing import Union
from .exceptions import *

async def generatecarbon(path="",code="Made with ❤ by Pranav Saxena",bg ="rgba(74, 144, 226, 100)",fontSize="14px",exportSize="2x",theme="seti",fontfamily="Hack",language= "auto",widthAdjustment:bool =True,linenumbers:bool= False,firstlinenumber:int= 1,lineheight:int = 130,paddingvertical= "56px",paddingHorizontal ="56px",squaredImage:bool = False,watermark:bool=False,dropShadow:bool= True,dropShadowBlurRadius="68px",dropShadowOffsetY ="20px",windowControls:bool = True,windowTheme:str = None):        
#-------------bool-check--------------------------------------------------    
    l={"widthAdjustment":widthAdjustment,"linenumbers":linenumbers,"squaredImage":squaredImage,"watermark":watermark,"dropShadow":dropShadow,"windowControls":windowControls}
    for i in l:
        if type(l[i])!=bool:
            raise notbool(f"{i} should be a boolean value(True/False)")
            return
#--------------------------InvalidExportSize-------
    if exportSize not in ["1x","2x","4x"]:
        raise InvalidExportSize("Export Size should be in [1x,2x,4x]")
#----------------InvalidSize------------
    l = {"Font Size":[fontSize,InvalidFontSize,"14px"],"Drop Shadow Blur Radius":[dropShadowBlurRadius,InvalidDropShadowBlurRadius,"68px"],"Drop Shadow Off Set Y":[dropShadowOffsetY,InvalidDropShadowOffsetY,"20px"],"Padding Vertical Input":[paddingvertical,InvalidPaddingVerticalInput,"56px"],"Padding Horizontal Input":[paddingHorizontal,InvalidPaddingHorizontalInput,"56px"]}
    for i in l:
        if len(l[i][0])<=2:
            raise l[i][1](f"{i} should be like '{l[i][2]}'")
            return
        elif l[i][0][-2:]!="px" or not l[i][0][:-2].isdigit():
            raise l[i][1](f"{i} should be like '{l[i][2]}'")
            return 
#--------theme---
    themedict = {"3024night":"3024-night","ally1dark":"a11y-dark","blackboard":"blackboard","base16dark":"base16-dark","base16light":"base16-light","cobalt":"cobalt","draculapro":"dracula-pro","duotonedark":"duotone-dark","hopscotch":"hopscotch","lucario":"lucario","material":"material","monokai":"monokai","nightowl":"night-owl","nord":"nord","oceanicnext":"oceanic-next","onelight":"one-light","onedark":"one-dark","panda":"panda-syntax","paraiso":"paraiso-dark","seti":"seti","shadesofpurple":"shades-of-purple","solarizeddark":"solarized+dark","solarizedlight":"solarized+light","synthwave84":"synthwave-84","twilight":"twilight","verminal":"verminal","vscode":"vscode","yeti":"yeti","zenburn":"zenburn"}
    temptheme = theme.lower().replace(" ","")
    temptheme = temptheme.replace("-","")
    temptheme = temptheme.replace("+","")
    if temptheme in themedict:
        theme = themedict[temptheme]
    else:
        theme = theme.lower()
#------------font-family-------
    fontdict = {"monolisa":"MonoLisa","dankmono":"dm","anonymouspro":"Anonymous+Pro","droidsansmono":"Droid+Sans+Mono","fantasquesansmono":"Fantasque+Sans+Mono","firacode":"Fira+Code","hack":"Hack","ibmplexmono":"IBM+Plex+Mono","inconsolata":"Inconsolata","iosevka":"Iosevka","jetbrainsmono":"JetBrains+Mono","monoid":"Monoid","sourcecodepro":"Source+Code+Pro","spacemono":"Space+Mono","ubuntumono":"Ubuntu+Mono"}
    tempfm = fontfamily.lower().replace(" ","")
    tempfm = tempfm.replace("-","")
    tempfm = tempfm.replace("+","")
    if tempfm in fontdict:
        fontfamily = fontdict[tempfm]
    else:
        fontfamily = fontfamily.lower()
#--------language----------
    langdict = {"apache":"text%2Fapache","bash":"application%2Fx-sh","plaintext":"text","c":"text%2Fx-csrc","cpp":"text%2Fx-c%2B%2Bsrc","c#":"text%2Fx-csharp","diff":"text%2Fx-diff","docker":"dockerfile","go":"text%2Fx-go","golang":"text%2Fx-go","html/xml":"htmlmixed","html":"htmlmixed","xml":"htmlmixed","java":"text%2Fx-java","json":"application%2Fjson","kotlin":"text%2Fx-kotlin","latex":"stex","stex":"stex","lisp":"commonlisp","matlab/octave":"text%2Fx-octave","matlab":"text%2Fx-octave","octave":"text%2Fx-octave","mysql":"text%2Fx-mysql","ntriples":"application%2Fn-triples","objectivec":"text%2Fx-objectivec","ocaml/f#":"mllike","ocaml":"mllike","f#":"mllike","php":"text%2Fx-php","riscv":"riscv","scala":"text%2Fx-scala","sparql":"application%2Fsparql-query","turtle":"text%2Fturtle","typescript":"application%2Ftypescript","tsx":"text%2Ftypescript-jsx","twig":"text%2Fx-twig","vb.net":"vb","yml":"yaml","vhd":"vhdl","ts":"application/typescript","ttl":"turtle","sc":"text/x-scala","scss":"sass","rslib":"rust","RData":"r","rds":"r","rda":"r","py":"python","pyc":"python","pyd":"python","pyo":"python","pyw":"python","pyz":"python","phtml":"text/x-php","php3":"text/x-php","php4":"text/x-php","php5": "text/x-php","php7":"text/x-php","phps":"text/x-php","php-s":"text/x-php","ps1":"powershell","ps1xml":"powershell","psc1":"powershell","psd1":"powershell","psm1":"powershell","pssc":"powershell","cdxml":"powershell","lisp":"commonlisp","cl":"commonlisp","lsp":"commonlisp","md":"markdown","nb":"mathematica","wl":"mathematica","nt":"ntriples","conf":"nginx","nim":"nimrod","m":"text/x-objectivec","mm":"text/x-objectivec","M":"text/x-objectivec","pp":"pascal","pas":"pascal","inc":"pascal","sh":"application%2Fx-sh","htaccess":"text/apache","cc":"text/x-c++src","cpp":"text/x-c++src","cxx":"text/x-c++src","c++":"text/x-c++src","hh":"text/x-c++src","hpp":"text/x-c++src","hxx":"text/x-c++src","h++":"text/x-c++src","cs":"text/x-csharp","clj":"clojure","cljs":"clojure","cljc":"clojure","edn":"clojure","cbl":"cobol","cob":"cobol","cpy":"cobol","coffee":"coffeescript","litcoffee":"coffeescript","cr":"crystal","kt":"text/x-kotlin","kts":"text/x-kotlin","jsx":"jsx","jar":"text/x-java","hs":"haskell","lhs":"haskell","hx":"haxe","hxml":"haxe","hbs":"handlebars","gql":"graphql","ml":"mllike","mli":"mllike","f":"fortran","for":"fortran","f90":"fortran","fs":"mllike","fsi":"mllike","fsx":"mllike","ex":"elixir","exs":"elixir","erl":"erlang","hrl":"erlang"}    
    templang = language.lower().replace(" ","")
    templang = templang.replace("-","")
    if templang in langdict:
        language = langdict[templang]
    else:
        language = language.lower()
#------------------colour----------------
    if bg.startswith('#') or len(bg) == 6:
        h = bg.lstrip('#')
        try:
            bg ='rgb'+str(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))
        except:
            pass
    
    url = f"https://carbon.now.sh/?code={code}&bg={bg}&fs={fontSize}&es={exportSize}&t={theme}&fm={fontfamily}&l={language}&wa={str(widthAdjustment).lower()}&ln={str(linenumbers).lower()}&fl={firstlinenumber}&pv={paddingvertical}&ph={paddingHorizontal}&si={str(squaredImage).lower()}&wm={str(watermark).lower()}&ds={str(dropShadow).lower()}&wt={str(windowTheme).lower()}&dsyoff={dropShadowOffsetY}&dsblur={dropShadowBlurRadius}&wc={windowControls}&lh={lineheight}%25"
    print("Generating carbon...")
    browser = await launch(defaultViewPort=None,
                           handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False,
                           headless=True,args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page._client.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': os.getcwd()
    })
    await page.goto(url, timeout=100000)
    element = await page.querySelector("#export-container  .container-bg")
    if path == "":
        path = "carbon.png"
    else:
        path = f"{path}/carbon.png"
    await element.screenshot({'path': f"{path}"})
    await browser.close()
    if path =="carbon.png":
        path = str(os.getcwd())+"\\"+"carbon.png"
    print(f"Carbon has been generated and saved at {path}")
