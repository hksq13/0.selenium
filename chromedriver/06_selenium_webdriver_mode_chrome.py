from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import  time
from selenium.webdriver.common.by import By



# et options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#disable webdriver_mode
options.add_argument("--disable-blink-features=AutomationControlled")

# user_agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")



s = Service(executable_path=r"D:\python_today_practice\0.selenium\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})


try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)
    
            
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()