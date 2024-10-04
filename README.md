<p align="center">
 <img src="images/logo.png" height="200"><br/>
A powerful XSS scanner made in python 3.7<br/>


## Installing

Requirements: <br/>

<li> Requirements </li>

```bash
pip install -r requirements.txt
```

Commands:

```bash
git clone https://github.com/rout369/vulntron.git
chmod 755 -R vulntron
cd vulntron
python3 vulntron.py  
```
## Usage
Basic usage:

```bash
python3 vulntron.py
```
For the Xss_Scanner:
```bash
python3 xssxplore.py --help
python3 xssxplore.py -u http://testphp.vulnweb.com
```


## Advanced usage
For the Xss_Scanner:
```bash
python3 xsscon.py --help
```

## Main features

* crawling all links on a website ( crawler engine )
* POST and GET forms are supported
* many settings that can be customized
* Advanced error handling
* Multiprocessing support.✔️
* ETC....


## Screenshot

<img src="images/screenshot.png">

## Roadmap

v0.3B:
------
<li> Added custom options ( --proxy, --user-agent etc... )</li>
<br/>

v0.3B Patch:
------
<li>Added support for ( form method GET ) </li>

v0.4B:
------
<li>Improved Error handling</li>
<li>Now Multiple parameters for GET method is Supported</li>

v0.5 Release (Final):
------
* Bug fixed
* Now cookies is supported. (--cookie {}) 
## Note
* Sorry for my bad english 
* if you run xsscon on the win10 terminal you will get an untidy output
* now it doesn't support DOM
