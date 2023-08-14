from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.request
import sys
from webdriver_auto_update import check_driver


url = "http://sso.lifepod.login/login?"
WebDriverLocation = "C:\\Users\\Tyan Nur\\AppData\\Local\\Programs\\Python\\Python311"


def connect(link):  # Fungsi untuk mencoba membuka link/url, jika gagal akan mengembalikan nilai false
    try:
        urllib.request.urlopen(link)
        return True
    except:
        return False


def checkChromeDriver(url):
    try:
        # Pass in the folder used for storing/downloading chromedriver
        check_driver(url)
    except Exception as e:
        print(e)


checkChromeDriver(WebDriverLocation)

""" membuat pageLoadStrategy
keterangan value :
"Strategy"	    "Ready State"	    "Notes"
normal          Complete            Used by default, waits for all resources to download
eager           Interactive         DOM access is ready, but other resources like images may still be loading
none            Any                 Does not block WebDriver at all """
options = Options()
options.page_load_strategy = 'eager'
web = webdriver.Chrome(options=options)


connect(url)


while not connect(url):
    web.refresh()
    sleep(5)
    connect(url)
else:
    web.get(url)
    curr_url = web.current_url
    sleep(1)
    if curr_url == 'https://jakwifi.lifepod.id/' or curr_url == 'https://jakwifi.lifepod.id/#gsc.tab=0':
        web.quit()
    else:
        NoHp = "085123456789"
        Hp = web.find_element(value='username')
        Hp.send_keys(NoHp)

        Password = "abcdef"
        password = web.find_element(value='userpassword')
        password.send_keys(Password)

        Tombol = web.find_element(by='xpath',
                                  value='/html/body/div/div/div[2]/div[2]/div/div/div/form/div/div/div[4]/input')
        Tombol.click()
        web.quit()

    print("Well Done")
    sys.exit()
