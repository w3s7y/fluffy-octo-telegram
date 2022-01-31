from django.test import TestCase
from rest_framework import status


class TestSnippets(TestCase):

    def test_valid_create_snippet_status_is_201(self):
        resp = self.client.post('/snippets/', {'id': '1', 'title': 'Testing snippet', 'code': 'echo "Hello world"'})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_try_create_bad_language_is_400(self):
        resp = self.client.post('/snippets/',
                                data={'language': 'Teasdet 2', 'code': 'echo "Hello"'})
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_java_language_snippet_is_200(self):
        resp = self.client.post('/snippets/',
                                data={'language': 'java', 'code': 'echo "Hello"'})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
