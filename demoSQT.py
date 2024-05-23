from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def verify_title():
    #Navigate to the website
    driver.get("https://sdetunicorns.com")

    #Get the title of the page
    title = driver.title

    #Verify the title
    expected_title="Master Softwre testing & Automation Online | SDET Unicorns"
    if title == expected_title:
        print ("Title verification successfull")
    else:
        print(f"Title verification failed. Expected'{expected_title}', but got '{title}'.")

    #Close the browser
    driver.quit()

#Press the green button in the gutter to run the script
if __name__ =='__main__':
    verify_title()
