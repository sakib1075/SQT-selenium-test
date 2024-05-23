from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

email = "sakib@gm.com"
password = "12121212"
url = "http://localhost/mysite/Project2/login.php"
driver.get(url)

sleep(1)

email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
email_input.send_keys(email)

password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
password_input.send_keys(password)
sleep(1)

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/input")))
submit_button.click()
sleep(1)

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/nav/a[4]")))
submit_button.click()
sleep(1)

#for pant
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[2]/section/div/form[1]/div/input[4]")))
submit_button.click()
'''#for shirt
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[2]/section/div/form[2]/div/input[4]")))
submit_button.click()
#for t-shirt
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[2]/section/div/form[3]/div/input[4]")))
submit_button.click()
#for tie
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[2]/section/div/form[4]/div/input[4]")))
submit_button.click()'''

print("Product add to cart successfully")
sleep(5)

driver.quit()