from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import  time

#options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=HelloMyWorld:)")



s = Service(executable_path=r"D:\python_today_practice\0.selenium\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

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
    driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent')
    
    time.sleep(10)
    # driver.get(url=url2)
    # time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()