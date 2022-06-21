import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password #django password_validation method
from django.test import TestCase

class TryDjangoConfigTest(TestCase):
        # https://docs.python.org/3/library/unittest.html
    def test_secret_key_strength(self):
        #settings.DEBUG 
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY, 'abc123')
        print(SECRET_KEY)
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak secret key{e.messages}'
            self.fail(msg)
        