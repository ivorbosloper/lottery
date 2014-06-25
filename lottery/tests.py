from django_webtest import WebTest
from django.test import TestCase
from lottery.models import Ticket
from django.test.testcases import LiveServerTestCase
from selenium import webdriver
import time


class ModelTest(TestCase):
    fixtures = ['tickets']

    def test_tostring(self):
        a = Ticket.objects.all()
        self.assertEquals(1, a.count())
        self.assertEquals("123", str(a[0]))


class FrontTest(LiveServerTestCase):
    fixtures = ['tickets']

    @classmethod
    def setUpClass(cls):
        super(FrontTest, cls).setUpClass()

        chromedriver = "/Users/ivor/dev/cropr_project/crop/testing/lib/chromedriver/chromedriver_mac32"
        options = webdriver.ChromeOptions()
        desired_capabilities = options.to_capabilities()
        desired_capabilities["chromeOptions"]["excludeSwitches"] = ["ignore-certificate-errors"]
        cls.driver = webdriver.Chrome(chromedriver, desired_capabilities=desired_capabilities)
        cls.driver.implicitly_wait(30)
        cls.driver.set_page_load_timeout(60)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        super(FrontTest, cls).tearDownClass()

    def _submit(self, number):
        driver = self.driver
        driver.get(self.live_server_url + "/")
        time.sleep(5)
        driver.find_element_by_id("id_number").clear()
        driver.find_element_by_id("id_number").send_keys(number)
        time.sleep(5)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def test_won(self):
        driver = self.driver
        self._submit('123')
        time.sleep(5)
        text = driver.find_element_by_css_selector("#result").text
        self.assertTrue('you won' in text, 'missing you won %s' % text)

    def test_not_won(self):
        driver = self.driver
        self._submit('1234')
        time.sleep(5)
        text = driver.find_element_by_css_selector("#result").text
        self.assertTrue('better luck' in text, 'missing better luck %s' % text)


import os
from subprocess import Popen, PIPE, STDOUT


class CasperTest(LiveServerTestCase):
    fixtures = ['tickets', ]

    def test_my_testcase(self):
        p = Popen(['casperjs test %s/casper/casper.coffee' % os.path.dirname(__file__)], shell=True, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print output
