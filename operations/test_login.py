import pytest
import pluggy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import allure
import time


@pytest.fixture()
def test_setup():
    global driver
    #driver = webdriver.Chrome(executable_path="C:\\Users\\Incise\\Desktop\\Selenium\\chromedriver.exe")
    serv_obj=Service("C:\\Users\\Incise\\Desktop\\Selenium\\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    driver.implicitly_wait(10)
    # driver.maximize_window()
    # yield
    # driver.quit()


@allure.description("Validate Automation Practice with valid credentials")
@allure.severity(severity_level="CRITICAL")
def test_validLogin(test_setup):
    driver.get("https://practicetestautomation.com/practice-test-login/");
    #driver.find_element(By.XPATH,"//header/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]").click();
    driver.find_element(By.ID,"username").clear();
    driver.find_element(By.ID,"password").clear();
    enter_username("student");
    enter_password("Password123");
    log("Clicking Login Button")
    driver.find_element(By.ID,"submit").click();
    #time.sleep(10)
    #assert "dashboard" in driver.current_url


@allure.description("Validate Automation Practice with invalid credentials")
@allure.severity(severity_level="NORMAL")
def test_invalidLogin(test_setup):
    driver.get("https://practicetestautomation.com/practice-test-login/");
    driver.find_element(By.ID,"username").clear();
    driver.find_element(By.ID,"password").clear();
    enter_username("Admin");
    enter_password("admin1234")
    log("Clicking login button")
    driver.find_element(By.ID,"submit").click();
    try:
        assert "dashboard" in driver.current_url
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(),
                          name="Invalid Credentials",
                          attachment_type=allure.attachment_type.PNG)


@allure.step("Entering Username as {0}")
def enter_username(username):
    driver.find_element(By.ID,"username").send_keys(username);


@allure.step("Entering Password as {0}")
def enter_password(password):
    driver.find_element(By.ID,"password").send_keys(password)


@allure.step("{0}")
def log(message):
    print(message)
