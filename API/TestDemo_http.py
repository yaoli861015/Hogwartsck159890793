# -*-coding:utf-8-*-
__author__ = 'YL'

import requests


class TestDemo:
    def test_http(self):
        re = requests.get('https://httpbin.testing-studio.com/get')
        print(re.text)
        print(re.json())
        print(re.status_code)
        assert re.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "yaoli"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "yaoli"
        }

        r = requests.post('https://httpbin.testing-studio.com/post', params=payload)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_header(self):
        r =
