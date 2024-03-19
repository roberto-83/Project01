#info , tutti i selector di slenium
#https://pythoninoffice.com/fixing-attributeerror-webdriver-object-has-no-attribute-find_element_by_xpath/

def readApiSito(user):
  # Configura ChromeDriver
  import sys
  import time

  sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

  # Importa le librerie necessarie
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.common.by import By

  # Configura le opzioni del browser Chrome
  chrome_options = Options()
  chrome_options.add_argument('--headless')  # Esegui Chrome in modalità headless
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument("--enable-javascript")
  chrome_options.add_argument('--disable-dev-shm-usage')

  # Inizializza il driver di Chrome
  driver = webdriver.Chrome( options=chrome_options)

  username = user.strip()
  password = user.strip()

  # Esempio di utilizzo
  driver.get('https://financeapi.net/dashboard')
  #print(driver.page_source)
  #prendo gli input
  username_field = driver.find_element(By.NAME,"username")
  password_field = driver.find_element(By.NAME,"password")
  #passo i parametri
  username_field.send_keys(username)
  password_field.send_keys(password)
  #print(driver.page_source)
  # Invia il modulo di login
  driver.find_element(By.XPATH,"//button[@type='submit']").click()
  time.sleep(5)
  #print(driver.title)
  #print(driver)
  #print(driver.page_source)
  apikey = driver.find_element(By.CLASS_NAME,"DashboardElements").find_element(By.TAG_NAME,"div").text
  apikey = apikey[9:len(apikey)]

  numapi = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div[1]/div[1]/div[3]').text
  #print(numapi[6:9].strip())#tolgo usage:
  numapi = numapi[6:9].strip()
  #numapi = numapi[6:10].strip()
  #substring del risultato

  #print(apikey)
  #print(numapi)

  #print(driver.find_element('class': 'DashboardElements'))
  #print(driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div[1]/div[1]/b'))

  # Chiudi il driver
  driver.quit()
  val = [apikey,numapi]
  return val

#val1 = readApiSito("robpol1983@gmail.com")
#print(val1)
#val2 = readApiSito("polegato.ro@gmail.com")
#print(val2)
#val3 = readApiSito("roberto.polegato@libero.it")
#print(val3)
