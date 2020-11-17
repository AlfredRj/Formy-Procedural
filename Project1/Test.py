from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com/")
action = ActionChains(driver)


#Test pertama
driver.find_element_by_css_selector(".btn.btn-lg").click()
complete = wait(driver,10).until(EC.visibility_of_element_located((By.ID, "autocomplete")))
complete.click()
complete.send_keys("Jalan Wadas Raya")
driver.implicitly_wait(2)
#Back to home
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test ke 2
Ke_Button = driver.find_element_by_xpath("/html/body/div[1]/div/li[2]/a")
Ke_Button.click()
driver.implicitly_wait(2)
buttonpath = driver.find_element_by_css_selector(".btn.btn-lg.btn-primary")
buttonpath.click()
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test ke 3
Ke_Check = driver.find_element_by_xpath("/html/body/div[1]/div/li[3]/a")
Ke_Check.click()
driver.implicitly_wait(2)
checkpath1 = driver.find_element_by_css_selector("input[value='checkbox-1']")
checkpath1.click()
checkpath2 = driver.find_element_by_css_selector("input[value='checkbox-2']")
checkpath2.click()
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test ke 4
Ke_Data = driver.find_element_by_xpath("/html/body/div[1]/div/li[4]/a")
Ke_Data.click()
driver.implicitly_wait(2)
datepath = driver.find_element_by_id("datepicker")
datepath.send_keys("11/11/20")
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test ke 5
Ke_Drag = driver.find_element_by_xpath("/html/body/div[1]/div/li[5]/a")
Ke_Drag.click()
driver.implicitly_wait(3)
imagepath = driver.find_element_by_xpath("/html/body/div[1]/div[1]/img")
boxpath = driver.find_element_by_id("box")
driver.implicitly_wait(0.5)
action.drag_and_drop(imagepath, boxpath).perform()
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test Ke 6
Ke_Upload = driver.find_element_by_xpath("/html/body/div[1]/div/li[8]/a")
Ke_Upload.click()
driver.implicitly_wait(2)
uploadpath = driver.find_element_by_id("file-upload-field")
buttonresetpath = driver.find_element_by_css_selector(".btn.btn-warning.btn-reset")
uploadpath.send_keys("Tugas3.docx")
buttonresetpath.click()
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test Ke 7
Ke_Input = driver.find_element_by_xpath("/html/body/div[1]/div/li[9]/a")
Ke_Input.click()
driver.implicitly_wait(2)
textboxpath = driver.find_element_by_id("name")
buttonconfirmpath = driver.find_element_by_id("button")
textboxpath.send_keys("Alfred Radja jaya")
buttonconfirmpath.click()
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test Ke 8
Ke_Scroll = driver.find_element_by_xpath("/html/body/div[1]/div/li[11]/a")
Ke_Scroll.click()
driver.implicitly_wait(2)
textboxscrollpath = driver.find_element_by_id("name")
datescrolpath = driver.find_element_by_id("date")
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
driver.implicitly_wait(2)
textboxscrollpath.click()
textboxscrollpath.send_keys("Alfred Radja Jaya")
datescrolpath.click()
datescrolpath.send_keys("16/11/2020")
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
#Test ke 9
Ke_Radio = driver.find_element_by_xpath("/html/body/div/div/li[12]/a")
Ke_Radio.click()
driver.implicitly_wait(2)
rb1path = driver.find_element_by_id("radio-button-1")
rb2path = driver.find_element_by_css_selector("input[value='option2']")
rb3path = driver.find_element_by_css_selector("input[value='option3']")
rb1path.click()
rb2path.click()
rb3path.click()
#BTH
logo = driver.find_element_by_id("logo")
logo.click()
driver.implicitly_wait(2)
# #Test Ke 10
# Ke_Modal = driver.find_element_by_xpath("/html/body/div[1]/div/li[10]/a")
# Ke_Modal.click()
# driver.implicitly_wait(2)
# buttonmodalpath = driver.find_element_by_id("modal-button")
# closemodalpath = driver.find_element_by_id("close-button")
# buttonmodalpath.click()
# driver.implicitly_wait(1)
# driver.execute_script("arguments[0].click();", closemodalpath)
# #BTH
# logo = driver.find_element_by_id("logo")
# logo.click()
# driver.implicitly_wait(2)
#Test ke 11
Ke_Multi = driver.find_element_by_xpath("/html/body/div[1]/div/li[13]/a")
Ke_Multi.click()
driver.implicitly_wait(2)
newtabpath = driver.find_element_by_id("new-tab-button")
newtabpath.click()
driver.implicitly_wait(2)
driver.switch_to.window(driver.window_handles[-1])





driver.close()

