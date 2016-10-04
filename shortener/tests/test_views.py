#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import ShortLink


class UserMixin(object):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='john', email='john@foo.com', password='top_secret'
        )
        self.client.force_authenticate(user=self.user)


class TestShortLinkViewSet(UserMixin, APITestCase):

    def setUp(self):
        super(TestShortLinkViewSet, self).setUp()
        self.obj = ShortLink.objects.create(original_url='http://foo.com/bar')
        self.obj2 = ShortLink.objects.create(id=300, original_url='http://foo.com/bar2')

    def test_create_link(self):
        url = reverse('shortener:shortlink-list')
        data = {'original_url': 'http://bar.com/aaa'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['original_url'], data['original_url'])
        self.assertTrue(response.data['hash'])

    def test_create_link_again(self):
        url = reverse('shortener:shortlink-list')
        data = {'original_url': 'http://foo.com/bar'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['original_url'], data['original_url'])
        self.assertTrue(response.data['hash'])


class TestGoToURLView(TestCase):

    def setUp(self):
        self.client = Client()
        self.obj = ShortLink.objects.create(original_url='http://foo.com/bar')

    def test_go_link(self):
        url = reverse('shortener:go', args=(self.obj.hash,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        self.assertIn(
            ('Location', 'http://foo.com/bar'),
            response.items(),
        )
