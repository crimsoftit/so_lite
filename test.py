from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # ensure landing page loads correctly
    def test_index_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index_has_text(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertTrue(b"Post a Question" in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertTrue(b'login successful', response.data)

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
                '/login',
                data=dict(username="admi", password="admin"),
                follow_redirects=True
            )
        self.assertTrue(b'invalid credentials. please try again' in response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
            )
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'you were logged out', response.data)

    def test_posts(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertTrue(b'ni yule mguyz' in response.data)

    def test_profile_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/profile', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
