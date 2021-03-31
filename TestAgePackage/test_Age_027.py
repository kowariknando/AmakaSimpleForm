from selenium import webdriver
import pytest
import data

driver = None

@pytest.fixture(scope='module') #this will be execute before and after each module
def setup():
    global driver
    PATH = "C:/Program Files (x86)/chromedriver.exe"  #path were is located the chromedriver
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://single-form.vercel.app/")

    driver.find_element_by_xpath(data.nameXPATH).send_keys("Fernando")
    driver.find_element_by_xpath(data.surnameXPATH).send_keys("Kowarik")
    driver.find_element_by_xpath(data.phoneXPATH).send_keys("+48 881-674-440")
    driver.find_element_by_xpath(data.websiteXPATH).send_keys("https://www.google.com/")
    driver.find_element_by_xpath(data.ageXPATH).send_keys("101")
    driver.find_element_by_xpath(data.buttonXPATH).click()

    yield driver
    driver.close() #We will close the browser after complete the tests.

#Validate proper notification message is showed if  Age is bigger 100

def test_TC_Age_027_Name(setup):
    messageName = driver.find_element_by_xpath(data.nameMessageXPATH)
    assert messageName.text == "Everything good"

def test_TC_Age_027_Surname(setup):
    messageSurname = driver.find_element_by_xpath(data.surnameMessageXPATH)
    assert messageSurname.text == "Everything good"

def test_TC_Age_027_Phone(setup):
    messagePhone = driver.find_element_by_xpath(data.phoneMessageXPATH)
    assert messagePhone.text == "Everything good"

def test_TC_Age_027_Website(setup):
    messageWebsite = driver.find_element_by_xpath(data.websiteMessageXPATH)
    assert messageWebsite.text == "Everything good"

def test_TC_Age_027_Age(setup):
    messageAge = driver.find_element_by_xpath(data.ageMessageXPATH)
    assert messageAge.text == "There we have some errors"