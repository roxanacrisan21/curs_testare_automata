# 1. Faceți o suita care sa contina testele voastre de la tema 9 + testele de la intalnirea 10
# (care au clasa). Generati raportul

from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner

from curs1.curs10.test3_alerts import Alerts
from curs1.curs10.test4_auth import Authentication
from curs1.curs10.test5_context_menu import ContextMenu
from curs1.curs10.test6_keys import Keyboard
from curs1.curs9.curs9tema import Login


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Tema10',
            report_name='Test Results'
        )

        runner.run(smoke_test)
