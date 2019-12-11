import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():

	@pytest.fixture
	def driver(self, request):
		driver_ = webdriver.Firefox()
		driver_.maximize_window()
		
		def quit():
			driver_.quit()

		request.addfinalizer(quit)
		return driver_

	def test_login_with_valid_credentials(self, driver, variables):
		driver.get("https://github.com/login")
		driver.find_element(By.ID, "login_field").send_keys(variables['valid_username'])
		driver.find_element(By.ID, "password").send_keys(variables['valid_password'])
		driver.find_element(By.NAME, "commit").click()

		driver.find_element(By.CSS_SELECTOR, ".dashboard-sidebar").is_displayed()
		driver.find_element(By.XPATH, "/html/body/div[1]/header/div[7]/details/summary").click()
		msg_text = driver.find_element(By.TAG_NAME, "strong").text		
		assert msg_text == variables['valid_username']

	def test_login_with_invalid_password(self, driver, variables):
		driver.get("https://github.com/login")
		driver.find_element(By.ID, "login_field").send_keys(variables['valid_username'])
		driver.find_element(By.ID, "password").send_keys(variables['invalid_password'])
		driver.find_element(By.NAME, "commit").click()

		msg_text = driver.find_element(By.CSS_SELECTOR, ".flash-error").text
		assert msg_text == "Incorrect username or password."
