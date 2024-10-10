import requests, json
##### Warna ####### 
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m' 
##### Styling ######
underline = "\033[4m"
##### Default ######
agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
line="—————————————————" 
#####################
def session(proxies, headers, cookie):
    """
    Create a requests session with specified proxies, headers, and cookies.

    Parameters:
    - proxies (dict): The proxies to use for the session.
    - headers (dict): The headers to include in the session.
    - cookie (str): A JSON string of cookies to set in the session.

    Returns:
    - requests.Session: Configured session object.
    """
    r = requests.Session()
    r.proxies = proxies
    r.headers = headers
    try:
        r.cookies.update(json.loads(cookie))
    except json.JSONDecodeError:
        print(f"{R}Error: Invalid cookie format.{N}")
    return r


logo=G+"""                      __   __        ___                          
                     /\ \ /\ \      /\_ \                         
 __  _   ____    ____\ `\`\/'/' ____\//\ \     ___   _ __    __   
/\ \/'\ /',__\  /',__\`\/ > <  /\ '__`\\ \ \   / __`\/\`'__\/'__`\ 
\/>  <//\__, `\/\__, `\  \/'/\`\\ \ \L\ \\_\ \_/\ \L\ \ \ \//\  __/ %s
 /\_/\_\/\____/\/\____/  /\_\\ \_\ \ ,__//\____\ \____/ \ \_\\ \____\
%s
 \//\/_/\/___/  \/___/   \/_/ \/_/\ \ \/ \/____/\/___/  \/_/ \/__/
                                   \ \_\                            
                                    \/_/

<<<<<<< STARTING >>>>>>>
"""%(R+"{v1.0 Devloping}"+G,underline+C+"https://github.com/rout369/vulntron"+N+G)
	
##=======
"""%(R+"{v1.0 Devloping}"+G,underline+C+"https://github.com/rout369/vulntron"+N+G)
	
>>>>>>> branch 'master' of https://github.com/rout369/vulntron
"""
