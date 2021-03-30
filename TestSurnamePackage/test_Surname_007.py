from selenium import webdriver
import pytest
import time
driver = None

@pytest.fixture(scope='module') #this will be execute before and after each method
def setup():
    global driver
    PATH = "C:/Program Files (x86)/chromedriver.exe"  #path were is located the chromedriver
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://single-form.vercel.app/")
    yield driver
    driver.close() #We will close the browser after complete the test method.


def test_TC_Surname_007(setup):
    driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[1]/input").send_keys("Fernando")
    driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[2]/input").send_keys("Ko")
    driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[3]/input").send_keys("+48 881-674-440")
    driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[4]/input").send_keys("https://www.google.com/")
    driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[5]/input").send_keys("29")
    driver.find_element_by_xpath("//*[@id='__next']/div/div/form/div[2]").click()


    messageName = driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[1]/div[3]")
    messageSurname = driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[2]/div[3]")
    messagePhone = driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[3]/div[3]")
    messageWebsite = driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[4]/div[3]")
    messageAge = driver.find_element_by_xpath("//*[@id='__next']/div/div/form/label[5]/div[3]")

    assert messageName.text == "Everything good"
    assert messageSurname.text == "There we have some errors"
    assert messagePhone.text == "Everything good"
    assert messageWebsite.text == "Everything good"
    assert messageAge.text == "Everything good"