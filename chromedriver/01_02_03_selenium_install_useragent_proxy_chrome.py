#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver
import  time
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password

user_agents_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 YaBrowser/23.1.0 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/109.0.5414.112 Mobile/15E148 Safari/604.1"
]

useragent = UserAgent()

#set options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# options.add_argument("user-agent=HelloMyWorld:)")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.117 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}") 
options.add_argument(f"user-agent={useragent.random}") 

#set proxy
# options.add_argument("--proxy-server=138.128.90.54:8000")

proxy_options = {
    "proxy" : {
        "https": f"http://{login}:{password}@138.128.90.54:8000"
    }
}


# s = Service(executable_path=r"D:\python_today_practice\0.selenium\chromedriver\chromedriver.exe")
# driver = webdriver.Chrome(service=s, options=options)
s = Service(executable_path=r"D:\python_today_practice\0.selenium\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s, seleniumwire_options=proxy_options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})

# url = "https://www.instagram.com/"
# url2 = "https://stackoverflow.com/"

try:
    driver.maximize_window()
    
    # avoid machine-detection pass
    # driver.get('https://anycoindirect.eu')
    
    #user-agent
    # driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent')
    # time.sleep(5)
    # driver.get(url=url2)
    # time.sleep(10)
    
    driver.get("https://2ip.ru")
    time.sleep(50)
    
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()