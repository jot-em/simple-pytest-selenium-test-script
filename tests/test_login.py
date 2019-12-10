import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():

	@pytest.fixture
	def driver(self, request):
		driver_ = webdriver.Firefox()

		def quit():
			driver_.quit()

		request.addfinalizer(quit)
		return driver_

	def test_invalid_password(self, driver):
		driver.get("https://github.com/login")