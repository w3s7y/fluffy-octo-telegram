from django.test import TestCase
import vets.views


class TestAuthentication(TestCase):
    """
    Class to group all tests related to authentication and authorization
    """
    def test_unathorised_get_on_api_with_no_creds(self):
        response = self.client.get('/vets/pets', follow=True)
        self.assertEqual(response.status_code, 403)

    def test_get_login_view_is_200(self):
        get_response = self.client.get('/api-auth/login', follow=True)
        self.assertEqual(get_response.status_code, 200)
