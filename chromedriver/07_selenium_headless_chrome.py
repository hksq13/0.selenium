from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import  time
from selenium.webdriver.common.by import By
from auth_data import vk_login, vk_password
import pickle


# set options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
# disable webdriver_mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
#options.headless = True


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
    driver.get("https://vk.com")
    time.sleep(5)  
    
    print("Passing authentification...")
    
    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys(vk_login)
    time.sleep(1)
    button_in = driver.find_element(By.CSS_SELECTOR,'[class="FlatButton FlatButton--primary FlatButton--size-l FlatButton--wide VkIdForm__button VkIdForm__signInButton"]')
    button_in.click()
    time.sleep(1)
    pass_in  = driver.find_element(By.NAME,'password')
    pass_in.clear()
    pass_in.send_keys(vk_password)
    time.sleep(1)
    button_pass = driver.find_element(By.CSS_SELECTOR,'[class="vkuiButton vkuiButton--sz-l vkuiButton--lvl-primary vkuiButton--clr-accent vkuiButton--aln-center vkuiButton--sizeY-compact vkuiButton--stretched vkuiTappable vkuiTappable--sizeX-regular vkuiTappable--hasHover vkuiTappable--hasActive vkuiTappable--mouse"]')
    button_pass.click()
    time.sleep(3)
    
    print("Going to the profile page...")
    
    driver.get("https://vk.com/vkclips")
    
    print("Start watching the video...")
    vk_klips_page = driver.find_element(By.CSS_SELECTOR,'[class="page_post_video_play_inline"]').click()
    time.sleep(5)
    print("Finish watching the video.")
    
            
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()