from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse


class TestMysiteApi(TestCase):
    def __init__(self):
        setup_test_environment()
        client = Client()


    def test_api_homepage_get_returns_get_response(self):
        """
        """
        rsp = client.get('/api/')
	self.assertIs(rsp, False)
	 
