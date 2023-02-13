from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import  time
from selenium.webdriver.common.by import By
import datetime 


# set options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
# disable webdriver_mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# options.headless = True


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
    start_time = datetime.datetime.now()
    
    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty")
    #print(driver.window_handles)
    print(f"Current url is: {driver.current_url}")
    # time.sleep(5)
    driver.implicitly_wait(5)
    
    items = driver.find_elements(By.XPATH, '//div[@data-marker="item"]')
    items[1].click()
    #print(driver.window_handles)
    # time.sleep(5)
    driver.implicitly_wait(5)
    
    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(5)
    driver.implicitly_wait(5)
    print(f"Current url is: {driver.current_url}")    
    
    username = driver.find_element(By.CSS_SELECTOR,'[class="style-seller-info-name-uWwYv js-seller-info-name"]')
    print(f"User name is: {username.text}")
    # time.sleep(5)
    driver.implicitly_wait(5)
    
    driver.close
    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(5)
    driver.implicitly_wait(5)
    print(f"Current url is: {driver.current_url}") 
    
    finish_time = datetime.datetime.now()
    
    spent_time = finish_time - start_time
    
    print(spent_time)
    print("#" * 20)
    print(f"Another metod in loop") 
    print("#" * 20)
    
    for i in range(5):
        items[i].click() #кликаем по карточке номер которой вышел в цикле
        driver.switch_to.window(driver.window_handles[-1]) #Переключаемся на последнюю открытую вкладку(-1 = последняя)
        print(driver.current_url) #выводим ссылку на влкадку
        #собираем и выводим информацию с открытой вкладки
        title = driver.find_element(By.CLASS_NAME, 'title-info-title-text')
        print(title.text)
        seller_geo = driver.find_element(By.CLASS_NAME, "style-item-address__string-wt61A")
        print(f'Локация: {seller_geo.text}')
        print()
        driver.close() #закрываем открытую вкладку

        driver.switch_to.window(driver.window_handles[0]) #переключаемся обратно на начальную вкладку
        time.sleep(2)    
  
    
        
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    
    "0:00:07.877296 - implicitly_wait"
    "0:00:56.925755 - sleep_time"