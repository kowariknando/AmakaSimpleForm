from selenium import webdriver
import pytest
import time
driver = None
import data

@pytest.fixture(scope='module') #this will be execute before and after each module
def setup():
    global driver
    PATH = "C:/Program Files (x86)/chromedriver.exe"  #path were is located the chromedriver
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://single-form.vercel.app/")

    driver.find_element_by_xpath(data.nameXPATH).send_keys("Thisisanamewiththirtycharacter")
    driver.find_element_by_xpath(data.surnameXPATH).send_keys("Kowarik")
    driver.find_element_by_xpath(data.phoneXPATH).send_keys("+48 881-674-440")
    driver.find_element_by_xpath(data.websiteXPATH).send_keys("https://www.google.com/")
    driver.find_element_by_xpath(data.ageXPATH).send_keys("29")
    driver.find_element_by_xpath(data.buttonXPATH).click()

    yield driver
    driver.close() #We will close the browser after complete the tests

#Validate proper notification message is showed if Name is exactly 30 characters

def test_TC_Name_004_Name(setup):
    messageName = driver.find_element_by_xpath(data.nameMessageXPATH)
    assert messageName.text == "There we have some errors"

def test_TC_Name_004_Surname(setup):
    messageSurname = driver.find_element_by_xpath(data.surnameMessageXPATH)
    assert messageSurname.text == "Everything good"

def test_TC_Name_004_Phone(setup):
    messagePhone = driver.find_element_by_xpath(data.phoneMessageXPATH)
    assert messagePhone.text == "Everything good"

def test_TC_Name_004_Website(setup):
    messageWebsite = driver.find_element_by_xpath(data.websiteMessageXPATH)
    assert messageWebsite.text == "Everything good"

def test_TC_Name_004_Age(setup):
    messageAge = driver.find_element_by_xpath(data.ageMessageXPATH)
    assert messageAge.text == "Everything good"
