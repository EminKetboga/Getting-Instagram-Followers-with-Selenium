import time
from selenium import webdriver


browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")

time.sleep(4)

k_adı = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
password = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

k_adı.send_keys("your information")
time.sleep(1)
password.send_keys("your information")
time.sleep(3)

giris = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")

giris.click()
time.sleep(10)
simdidegil = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
time.sleep(3)
simdidegil.click()

time.sleep(2)



smd2 = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
time.sleep(4)
smd2.click()

time.sleep(1)

profile = browser.find_element_by_css_selector(".gmFkV")
profile.click()
time.sleep(3)

buttonlar = browser.find_elements_by_css_selector("._7UhW9.vy6Bb.MMzan.KV-D4.uL8Hv.T0kll")
takipci_button = buttonlar[1]
takipci_button.click()
time.sleep(4)
jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(2)
takipciler = browser.find_elements_by_css_selector(".notranslate._0imsa")
sayi = 1
with open("TümTakipçiler2.txt","w",encoding= "UTF-8") as file:
    for takipci in takipciler:
        file.write("********** " + str(sayi) + ".Takipçi **********\n" + takipci.text + "\n")
        sayi += 1

time.sleep(5)

browser.close()

