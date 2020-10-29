from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

driver_path = "d:\\download\chromedriver.exe"
extenstion_path = r'C:\project\personal_scrapper\0.9.5.25_0'

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('load-extension=' + extenstion_path)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(driver_path, options=chrome_options)
driver.create_options()
driver.set_window_size(1280, 768)
driver.get('https://poong.today/')

search_box = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="main_chart_controler"]/div[2]/input'))
)


bj_array = ['하한국영', 'monov', '해범', 's2apple', '혀니츄', '커맨더지코']


def search_bj(name):
    search_box.send_keys(name)
    daily_balloon = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'chart-day-balloon')))

    monthly_balloon = driver.find_element_by_class_name('chart-month-balloon')
    poong_per_hour = driver.find_element_by_class_name('chart-month-pay')

    print(f"TODAY   :: {name} has got donation of {daily_balloon.text} today")
    print(
        f"MONTHLY :: {name} has got donation of {monthly_balloon.text} this month")
    print(f"P/H     :: {name} has earned {poong_per_hour.text} per hour")

    print("=================================================")
    search_box.clear()


for bj in bj_array:
    search_bj(bj)

driver.close()
