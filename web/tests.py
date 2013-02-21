"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class MochadTest(TestCase):
    def test_basic_command(self):
        from web import netcat
        print netcat.command("pl a5 off")
