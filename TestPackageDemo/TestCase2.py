import unittest
from selenium import webdriver


def setUpModule(): #be executed before executing any class or any method present in the test class
    print("setUpModule")

def tearDownModule(): #will be executed after completing everything present in the python module
    print("tearDownModule")

    

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): #execute before each def
        print("This is the login test part of the setup")

    @classmethod
    def tearDown(self): #execute after each def
        print("this is the tear Down decorator to close")

    @classmethod
    def setUpClass(cls):
        print("This is def to open the application SetUpClass")

    @classmethod
    def tearDownClass(cls): #execute when the class started
        print("After completation of each class method this is the TearDown")

    def test_search(self): #execute when the class finished
        print("this is search test")

    def test_advancesearch(self):
        print("this is Advance search test")

    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of this page is  : " + self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("The title of Bing is  : " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()