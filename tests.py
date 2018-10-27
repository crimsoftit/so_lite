import unittest
from flask_testing import TestCase
from flask_login import current_user
from project import app, db
from project.models import BlogPost, User


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object("config.TestConfig")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(BlogPost('kevo', 'ni yule mguyz'))
        db.session.add(User("admin", "ad@min.com", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # ensure landing page loads correctly
    def test_landing_page_loads(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index_has_text(self):
        response = self.client.get('/', content_type="html/text")
        self.assertTrue(b"Post a Question" in response.data)

    def test_posts(self):
        response = self.client.get('/', content_type="html/text")
        self.assertTrue(b'ni yule mguyz' in response.data)

    def test_profile_route_requires_login(self):
        response = self.client.get('/profile', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)


class UsersViewsTests(BaseTestCase):

    def test_signup_page_loads(self):
        response = self.client.get("/signup", content_type="html/text")
        self.assertTrue(response.status_code, 200)

    def test_correct_signup(self):
        with self.client:
            response = self.client.post(
                "/signup",
                data=dict(
                    username="manu",
                    email="sindani254@gmail.com",
                    password="Soen@30010010",
                    confirm="Soen@30010010"
                ), 
                follow_redirects=True
            )
            self.assertTrue(current_user.name == "manu")
            self.assertTrue(current_user.is_active())

    def test_login_page_loads(self):
        response = self.client.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login', data=dict(username='admin', password='admin'),
                follow_redirects=True
            )
            self.assertTrue(b'login successful', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active)

    def test_incorrect_login(self):
        response = self.client.post(
                '/login',
                data=dict(username="admi", password="admin"),
                follow_redirects=True
            )
        self.assertTrue(b'invalid credentials. please try again' in response.data)

    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertTrue(b'you were logged out', response.data)
            self.assertFalse(current_user.is_active)


if __name__ == "__main__":
    unittest.main()
