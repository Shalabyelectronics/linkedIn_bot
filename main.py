from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import shutil
import os

CHROME_DRIVER = os.environ.get("CHROMEDRIVER")
Download_path = r"C:\Users\dalla\.wdm\drivers\chromedriver\win32"

try:
    service = Service(executable_path=CHROME_DRIVER)
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
except Exception as r:
    CHROM_VERSION = ChromeDriverManager().driver.get_version()
    service = Service(executable_path=ChromeDriverManager().install())
    shutil.move(os.path.join(Download_path, CHROM_VERSION, "chromedriver.exe"), r"C:\WebDriver\bin")
    driver = webdriver.Chrome()

driver.implicitly_wait(time_to_wait=60)
driver.maximize_window()
driver.get("https://www.linkedin.com/login/ar?trk=homepage-basic_ispen-login-button")
LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASS = os.environ.get("LINKEDIN_PASS")


def sign_in_linkedIn():
    user_name = driver.find_element(By.NAME, 'session_key')
    user_name.send_keys(LINKEDIN_EMAIL + Keys.TAB)
    password = driver.find_element(By.NAME, 'session_password')
    password.send_keys(LINKEDIN_PASS + Keys.TAB)
    submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    submit_button.click()


def search_jobs(job_title):
    jobs_button = driver.find_element(By.ID, "ember20")
    jobs_button.click()
    search_entry = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
    search_entry.clear()
    search_entry.send_keys(job_title + Keys.ENTER)
    for job_number in range(1, 26):
        driver.find_element(By.XPATH,
                            f'/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{job_number}]/div/div').click()
        WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div['
                                                                                 '3]/div[2]/div/section['
                                                                                 '2]/div/div/div[1]/div/div[ '
                                      '1]/div/div[2]/div[3]/div/button')))

        driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div['
                                      '1]/div/div[2]/div[3]/div/button').click()
    jobs_button.click()
    check_saved_jobs = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[3]/div/div/div/div/div/div[1]/nav/div/ul/li[1]/a/span')
    check_saved_jobs.click()


sign_in_linkedIn()
search_jobs("Python Developer")
time.sleep(60 * 5)
driver.delete_all_cookies()
driver.close()
driver.quit()
