import unittest

from ok import Key


class KeyTest(unittest.TestCase):

    def test_key(self):
        class User(Key):
            pass

        self.assertEqual(User().key, 'User')

    def test_field_access(self):
        class User(Key):
            fields = ['timeline', 'followers', 'following']

        self.assertEqual(User('mixxorz').timeline, 'User:mixxorz:timeline')

    def test_class_key_access(self):
        class User(Key):
            pass

        self.assertEqual(User('mixxorz').key, 'User:mixxorz')

    def test_subkey_access(self):
        class City(Key):
            pass

        class Province(Key):
            subkeys = [City]

        class Country(Key):
            subkeys = [Province]

        self.assertEqual(Country('PH').Province('Metro Manila').City('Manila').key,  # noqa
                         'Country:PH:Province:Metro Manila:City:Manila')

    def test_string_subkey_access(self):
        self.assertEqual(Parent('foo').Refer('bar').key,
                         'Parent:foo:Refer:bar')

    def test_empty_id(self):
        class Twitter(Key):
            fields = ['tweets']

        self.assertEqual(Twitter().tweets, 'Twitter:tweets')

    def test_class_key(self):
        class Twitter(Key):
            class_key = 'twitter'

        self.assertEqual(Twitter().key, 'twitter')


class Parent(Key):
    subkeys = ['ok.tests.Refer']


class Refer(Key):
    pass
