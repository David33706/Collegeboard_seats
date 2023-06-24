
import time
import pytz
from selenium.webdriver.chrome.options import Options
from datetime import datetime

chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
country_time = pytz.timezone('Asia/Tashkent')

chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")

n = -1
n1 = -1

# Server details
PATH = Service('/home/Collegeboard_project/Chrome_files/chromedriver')
username = "dohngrane@gmail.com"
password = "Dovudxon2006!"

MR_path = '/home/Collegeboard_project/Kyrgyzstan/March_Kyrgyzstan.txt'
MY_path = '/home/Collegeboard_project/Kyrgyzstan/May_Kyrgyzstan.txt'
JN_path = '/home/Collegeboard_project/Kyrgyzstan/June_Kyrgyzstan.txt'
DC_path = '/home/Collegeboard_project/Kyrgyzstan/December_Kyrgyzstan.txt'


# Success and failure
def success(n1):
    now = datetime.now(country_time)
    n1 += 1
    return ("Executed successfully\n" + str(n1) + ' ' + str(now))


def failure(n):
    now = datetime.now(country_time)
    n += 1
    return ("Programm was turned off\n" + str(n) + ' ' + str(now))


# View results
def num(a):
    n = a.split()
    s = ''
    for i in n[2]:
        if i.isdigit():
            s += i
    if int(s) % 5 == 0:
        return int(s) // 5
    else:
        return (int(s) // 5) + 1


# Gaining August details
def March():
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'test-center-date-button-MAR-11')))
    element.click()

    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "testdate-continue-button")))
    time.sleep(0.5)
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button")))
    time.sleep(1)
    element.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='results-label cb-roboto-medium']")))
    n = num(element.text)
    info = ''
    for i in range(n):
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "undefined_" + str(i))))
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "table-select-btn")))

        href = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-lg-12 col-xs-12 test-center-label']/a")))
        for i in range(len(element)):
            info += (element[i]).text + '\n'
            info += (href[i]).get_attribute('href')
            info += '\n\n'

    now = datetime.now(country_time)
    MR = open(MR_path, 'w')
    MR.write('March 11' + '\n\n' + info + 'Last time checked at: ' + now.strftime("%H:%M:%S"))
    MR.close()

    # Return to choosing date
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/a")))
    time.sleep(0.5)
    element.click()


# Gaining October details
def May():
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'test-center-date-button-MAY-6')))
    element.click()

    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "testdate-continue-button")))
    time.sleep(0.5)
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button")))
    time.sleep(1)
    element.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='results-label cb-roboto-medium']")))
    n = num(element.text)
    info = ''
    for i in range(n):
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "undefined_" + str(i))))
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "table-select-btn")))

        href = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-lg-12 col-xs-12 test-center-label']/a")))
        for i in range(len(element)):
            info += (element[i]).text + '\n'
            info += (href[i]).get_attribute('href')
            info += '\n\n'

    now = datetime.now(country_time)
    MY = open(MY_path, 'w')
    MY.write('May 6' + '\n\n' + info + 'Last time checked at: ' + now.strftime("%H:%M:%S"))
    MY.close()

    # Return to choosing date
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/a")))
    time.sleep(0.5)
    element.click()


# Gaining december details
def June():
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'test-center-date-button-JUN-3')))
    element.click()

    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "testdate-continue-button")))
    time.sleep(0.5)
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button")))
    time.sleep(1)
    element.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='results-label cb-roboto-medium']")))
    n = num(element.text)
    info = ''
    for i in range(n):
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "undefined_" + str(i))))
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "table-select-btn")))

        href = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-lg-12 col-xs-12 test-center-label']/a")))
        for i in range(len(element)):
            info += (element[i]).text + '\n'
            info += (href[i]).get_attribute('href')
            info += '\n\n'

    now = datetime.now(country_time)
    JN = open(JN_path, 'w')
    JN.write('June 3' + '\n\n' + info + 'Last time checked at: ' + now.strftime("%H:%M:%S"))
    JN.close()

    # Return to choosing date
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/a")))
    time.sleep(0.5)
    element.click()
def Dec():
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'test-center-date-button-DEC-3')))
    element.click()

    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "testdate-continue-button")))
    time.sleep(0.5)
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div[3]/div/div[3]/div/div/div[3]/button")))
    time.sleep(1)
    element.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='results-label cb-roboto-medium']")))
    n = num(element.text)
    info = ''
    for i in range(n):
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "undefined_" + str(i))))
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "table-select-btn")))

        href = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-lg-12 col-xs-12 test-center-label']/a")))
        for i in range(len(element)):
            info += (element[i]).text + '\n'
            info += (href[i]).get_attribute('href')
            info += '\n\n'

    now = datetime.now(country_time)
    DC = open(DC_path, 'w')
    DC.write('December 3' + '\n\n' + info + 'Last time checked at: ' + now.strftime("%H:%M:%S"))
    DC.close()

    # Return to choosing date
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                              "/html/body/div[1]/div[2]/div/div[2]/div/div[6]/div/div/div[3]/div/div[1]/div/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/a")))
    time.sleep(0.5)
    element.click()

while True:
    try:
        # Getting into site
        driver = webdriver.Chrome(service=PATH, options=chrome_options)
        driver.get(
            "https://account.collegeboard.org/login/login?appId=424&DURL=https://mysat.collegeboard.org/dashboard&idp=ECL")

        # Login and password
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "idp-discovery-username")))
        print('connected')

        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "idp-discovery-username")))
        element.send_keys(username)


        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "idp-discovery-submit")))
        element.click()

        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "okta-signin-password")))
        element.send_keys(password)

        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "okta-signin-submit")))
        element.click()


        # Register for SAT

        element = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.ID, "qc-id-header-register-button")))
        element.click()

        time.sleep(1.5)

        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='cb-btn cb-btn-yellow interstitial-primary']")))
        time.sleep(1)
        element.click()
        print('success till save button')
        # Personal information
        time.sleep(2)
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "grade-save-button")))
        element.click()

        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "graddate-save-button")))
        element.click()

        # Demographics
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "continue-to-demographics-btn")))
        time.sleep(1.5)
        element.click()
        for i in range(3):
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "save-exit-demographics-btn")))
                element.click()
                break
            except:
                print("Exception with continue to demohraphics")

                continue

        # Test date confirmation
        time.sleep(2)

        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='cb-btn cb-btn-yellow interstitial-primary']")))
        element.click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "terms-desc")))
        element.send_keys(Keys.END)
        for i in range(8):
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[@class='cb-span']")))
                time.sleep(1)
                element.click()
                element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "forward-btn")))
                element.click()
                element = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.ID, "testlocation-continue-button")))
                time.sleep(0.5)
                element.click()
                break
            except:
                time.sleep(3)
                print("Exception with agree terms happened")
        print("Success till the date!")
        for i in range(10):
            March()
            time.sleep(70)
            May()
            time.sleep(70)
            June()
            time.sleep(70)
            n1 += 1
        print("Terminated after 3 and half hours of work")
        time.sleep(30)




    except:

        n += 1
        print(failure(n))

        try:
            driver.close()
            driver.quit()
            time.sleep(50)
        except:
            print("Driver turned off because of memory fill")
            time.sleep(40)
