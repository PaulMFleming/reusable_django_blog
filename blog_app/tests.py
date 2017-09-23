# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
# the dot (.) before models means that models is in
# the same dir as this file
from .models import Post

# Create your tests here.
class PostTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post model
    to run the tests:
    python manage.py test blog_app
    """

    # creates an instance of the Post class and initializes it
    # with a title and saves it to the test_titile variable
    # then uses assertEqual to check that our title is as expected
    def test_str(self):
        test_title = Post(title="My Latest Blog Post")
        self.assertEqual(str(test_title),
                        'My Latest Blog Post')
