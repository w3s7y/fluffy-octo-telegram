from django.test import TestCase

class TestRestApi(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    
    def test_unauthenticated_get_on_users_api(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 403)
        
        
    def test_unauthenticated_get_on_groups_api(self):
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, 403)
        
        
    def test_redirect_in_users_uri(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 301)
        
        
    def test_redirect_in_groups_uri(self):
        response = self.client.get('/groups')
        self.assertEqual(response.status_code, 301)

