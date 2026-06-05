from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
taipei="臺北市區監理所（含金門馬祖）"
shilin="士林監理站(臺北市士林區承德路5段80號)"
        #test places
chiayi="嘉義區監理所（雲嘉南）"
chiayi_place1="嘉義區監理所(嘉義縣朴子市朴子七路29號)"
taichung="臺中區監理所（中彰投）"
taichung_place1="豐原監理站(臺中市豐原區豐東路120號)"
time_test="1150115" #year month day in taiwan year (115=2026)

driver=webdriver.Chrome()
wait = WebDriverWait(driver, 1)

def load_website():
    driver.get("https://www.mvdis.gov.tw/m3-emv-trn/exm/locations#gsc.tab=0")

def click():
    search_button = driver.find_element(By.XPATH, "//a[@onclick='query();']")
    search_button.click()

def aware():
    #wait = WebDriverWait(driver, 1)
    print("ui AWARENESS")
    ####---- Make sure that we used it right cause it is a nested <a> tag
    search_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), '選擇場次繼續報名')])[last()]")))
    search_button2.click()
######-------------------------------------------------#######
def choose_date_time_place():
    input_el= driver.find_element(By.ID,"licenseTypeCode")
    input_el.click()
    #wait = WebDriverWait(driver, 0.2)
    #time.sleep(0.2)

                    #type of test
    select_el = Select(driver.find_element(By.ID, "licenseTypeCode"))
    
                    #select_el.select_by_value("普通重型機車")
    for option in select_el.options:
        print(f"Value: {option.get_attribute('value')}, Text: {option.text}")# to see the options
    select_el.select_by_visible_text("普通重型機車")#bc by value doesnt work


                    #place of test
    select_el2 = Select(driver.find_element(By.ID, "dmvNoLv1"))
    select_el2.select_by_visible_text(taipei)
    #time.sleep(2)


    #selecting shilin
    #wait for the option to appear
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "dmvNo"))
    )
    #select the location
    select_el3 = Select(driver.find_element(By.ID, "dmvNo"))
    select_el3.select_by_visible_text(shilin)
    time.sleep(0.2)
    #   date
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "expectExamDateStr"))
    )
    select_el4=(driver.find_element(By.ID,"expectExamDateStr"))
    select_el4.send_keys(time_test)
    time.sleep(0.2)
    print("yes")

def fill_form(name:str,phone:str,email:str,id:str,bday:str):
    #1-  ID num
    select_el4=(driver.find_element(By.ID,"idNo"))
    select_el4.send_keys(id)
    #   BIRTHDAY
    select_el4=(driver.find_element(By.ID,"birthdayStr"))
    select_el4.send_keys(bday)
    #   NAME
    select_el4=(driver.find_element(By.ID,"name"))
    select_el4.send_keys(name)
    #   PHONE

    select_el4=(driver.find_element(By.ID,"contactTel"))
    select_el4.send_keys(phone)

    #   EMAIL
    select_el4=(driver.find_element(By.ID,"email"))
    select_el4.send_keys(email)
    #time.sleep(10)
    
def signup_place():
    signUp = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), '報名 SignUp')])[1]")))
    signUp.click()
    signUp = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(), '我已充分知悉相關約定並願接受')])[last()]")))
    signUp.click()






user1={'name':'',' Phone number':'','id_num_arc':'','birth_d_Taiwan year':'','email':''}



users=[user1]
counter=0
for user in users:
    load_website()
    time.sleep(10)
    choose_date_time_place()
    click()
    aware()
    #time.sleep(2)
    signup_place()
    fill_form(user['name'],user['number'],user['email'],user['id_num'],user['birth_d'])
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    time.sleep(20)
    counter+=1
    if counter>=2:
        time.sleep(5000)

