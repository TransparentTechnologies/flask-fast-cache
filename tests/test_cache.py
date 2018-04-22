"""Unit Test for Cloud Realty"""
import os
import unittest
from flask import url_for
from tests import BaseTest


class CommonTests(object):

    def test_set_cache(self):
        set_cache = self.cache.set('test_key', ['a', 'b', 'c'])
        self.assertTrue(set_cache)

    def test_get_cache(self):
        set_cache = self.cache.set('test_key', ['a', 'b', 'c'])
        self.assertTrue(set_cache)
        get_cache = self.cache.get('test_key')
        self.assertEqual(get_cache, ['a', 'b', 'c'])

    def test_delete_cache(self):
        set_cache = self.cache.set('test_key', ['a', 'b', 'c'])
        self.assertTrue(set_cache)
        get_cache = self.cache.get('test_key')
        self.assertEqual(get_cache, ['a', 'b', 'c'])
        self.cache.delete('test_key')
        get_cache = self.cache.get('test_key')
        self.assertFalse(get_cache)

    def test_delete_wildcard(self):
        set_cache = self.cache.set('test_key:1', ['a', 'b', 'c'])
        self.assertTrue(set_cache)
        get_cache = self.cache.get('test_key:1')
        self.assertEqual(get_cache, ['a', 'b', 'c'])
        set_cache = self.cache.set('test_key:2', ['a', 'b', 'c'])
        self.assertTrue(set_cache)
        get_cache = self.cache.get('test_key:2')
        self.assertEqual(get_cache, ['a', 'b', 'c'])
        self.cache.delete_wildard('test_key')
        get_cache = self.cache.get('test_key:1')
        self.assertFalse(get_cache)
        get_cache = self.cache.get('test_key:2')
        self.assertFalse(get_cache)


class TestFileCache(BaseTest, CommonTests):

    def setUp(self):
        os.environ['CACHE_TYPE'] = 'file'
        super().setUp()

class TestNullCache(BaseTest, CommonTests):

    def setUp(self):
        os.environ['CACHE_TYPE'] = 'null'
        super().setUp()
        
    def test_get_cache(self):
        set_cache = self.cache.set('test_key', ['a', 'b', 'c'])
        self.assertTrue(set_cache)
        get_cache = self.cache.get('test_key')
        self.assertFalse(get_cache)
    
    def test_delete_cache(self):
        pass
        
    def test_delete_wildcard(self):
        pass    
        
class TestRedisCache(BaseTest, CommonTests):

    def setUp(self):
        os.environ['CACHE_TYPE'] = 'redis'
        super().setUp()
        