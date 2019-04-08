import requests
import logging
import bs4

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import webbrowser
import subprocess, sys


my_path = os.path.abspath(os.path.dirname(__file__))
#launch putty and calculator then continure
def apps():
#os.system('start putty.exe & calc.exe')
    username = ""
    password = ""
    p = subprocess.Popen(['powershell.exe', "-ExecutionPolicy", "RemoteSigned",
                          "-File","C:\\Users\\markr\\OneDrive\\Desktop\\apps.ps1", username, password],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.communicate()

#open files
def files():
    path = os.path.join(my_path,"workfiles.txt")
    openf = open("workfile.txt")
    for fname in openf:
        values = fname.rstrip()
        print values
        os.startfile(values)
    openf.close()

#open links
def links():
    path = os.path.join(my_path,"worklinks.txt")
    openl = open(path)
    for link in openl:
        values = link.rstrip()
        print values
        browser_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(browser_path))
        webbrowser.get('chrome').open_new(values)

#my.ti.com
def myti():
    payload = {
        'exmyTIEmail': '',
        'exmyTIPassword': ''
    }
    useragent = {'User-Agent': 'Mozilla/5.0'}
    session_requests = requests.session()
    session_requests.verify = False
    login = 'https://ti-pass.ext.ti.com/cgi-bin/login/plogin.pl'
    loggedin = 'https://ti-pass.ext.ti.com/cgi-bin/login/warning.pl?lt=myti2&OKPage=https%3A%2F%2Fmy.ti.com%2F&warn=1'
    #res = session_requests.get(host, verify=False, headers=useragent)

    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    verifylogin = session_requests.post(login, data=payload)
    alreadyloggedin = session_requests.get(loggedin)

    print(verifylogin.status_code)
    print(alreadyloggedin.status_code)

    # print(acontent)
    soup = bs4.BeautifulSoup(alreadyloggedin.text, 'html.parser')
    #print(alreadyloggedin.text)
    print (soup.prettify())
"""
    #web Driver chrome
    driver = webdriver.Chrome()
    driver.get(loggedin)

    #press continue button
    cont_btn = driver.find_element_by_id('continuebutton')
    cont_btn.click()
    driver.get("https://myinfolink.ti.com/")
"""
myti()
"""
#ldap
def ldap():   
#xid
def xid():
#diradmin
def diradmin():
"""