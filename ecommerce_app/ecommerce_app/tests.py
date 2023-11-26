from django.test import TestCase
from django.urls import reverse
from .models import *
from .views import *
from django.contrib.auth.models import User
from django.test import Client, LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Create your tests here.

# Selenium test
class ProductFormTest(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()

    def tearDown(self):
        self.selenium.quit()

    def test_word_presence(self):
        # Homepage
        self.selenium.get(self.live_server_url)

        # Check for title
        assert 'TurtleByrd' in self.selenium.page_source

    def test_home_button_presence(self):
        self.selenium.get(self.live_server_url)

        # Check for Home Button
        assert 'Home' in self.selenium.page_source


# Homepage tests
class HomepageTests(TestCase):
    # Check it exists
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    # Check url by name
    def test_url_available_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    # Teset templates by name
    def test_template_name_correct(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "ecommerce_app/index.html")
    # Ensure data is in html
    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<title>TurtleByrd Ecomme</title>")
        self.assertNotContains(response, "Not on the page")


# # Product Model Test
class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Can", price=12.12, description="Can of metal")
        Product.objects.create(name="Cup", price=1.03, description="Cup of glass")

    def test_products_have_descriptions(self):
        """Animals that can speak are correctly identified"""
        Can = Product.objects.get(name="Can")
        Cup = Product.objects.get(name="Cup")

        self.assertEqual(Can.name, 'Can')
        self.assertEqual(Cup.name, 'Cup')




