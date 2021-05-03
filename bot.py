from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from playsound import playsound

import os

scriptdir = os.path.dirname(os.path.realpath(__file__))
PATH = scriptdir+"\chromedriver.exe"
options = Options()
#options.add_argument("user-data-dir="+scriptdir+"\profile")
driver = webdriver.Chrome(PATH,options=options)

RTX3070LINK1 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
driver.get(RTX3070LINK1)

isComplete = False

while not isComplete:

    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found")

    # add to cart
    atcBtn.click()

    print("Now you are in queue. The checkout is up to you :)")
    playsound(scriptdir+"\woohoo.wav")
	
    isComplete = True
