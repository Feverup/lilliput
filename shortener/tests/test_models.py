#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from django.test import TestCase
from ..models import ShortLink


class TestShortLinkModel(TestCase):

    def setUp(self):
        self.obj = ShortLink.objects.create(original_url='http://foo.com/bar')
        self.obj2 = ShortLink.objects.create(id=300, original_url='http://foo.com/bar2')

    def test_first_hash(self):
        self.assertEqual(self.obj.hash, '1')

    def test_last_hash(self):
        self.assertEqual(self.obj2.hash, '4i')
