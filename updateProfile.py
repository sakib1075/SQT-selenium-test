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

email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
email_input.send_keys(email)

password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
password_input.send_keys(password)

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/form/input")))
submit_button.click()

profile_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/nav/a[1]")))
profile_link.click()

update_profile_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[2]/section/form/div[2]/a[1]")))
update_profile_link.click()

name_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "name")))
name_input.clear()
name_input.send_keys("rakib")

email_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "email")))
email_input.clear()
email_input.send_keys("rakib@gmail.com")

phone_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "number")))
phone_input.clear()
phone_input.send_keys("09876543211")

print("Update profile successfully")
sleep(5)

driver.quit()