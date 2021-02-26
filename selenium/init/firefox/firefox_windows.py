from selenium import webdriver

class RunTests:
    def testMethod(self):
        driver = webdriver.Firefox(executable_path="C:\\Automation\\selenium\\drivers\\geckodriver.exe")
        driver.get('http://www.google.com')

ff = RunTests()
ff.testMethod()