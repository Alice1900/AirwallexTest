import requests


class Request:

    def __init__(self, url):
        self.url = url

    def post_request(self, data):
        response = requests.post(self.url, json=data)
        return response
