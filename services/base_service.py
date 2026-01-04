import requests

class BaseService():
    def get(self, url, payload = None, headers = None):
        return requests.get(url, json = payload, headers = headers)

    def post(self, url, payload = None, headers = None):
        return requests.post(url, json = payload, headers = headers)

    def put(self, url, payload = None, headers = None):
        return requests.put(url, json = payload, headers = headers)

    def delete(self, url, headers = None):
        return requests.delete(url, headers = headers)