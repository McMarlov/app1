import requests
from requests.api import request
params = {"inp_author": "Adic3",
        "inp_quote": "Citata"}
print(requests.get('http://127.0.0.1:5000'))
print(requests.post('http://127.0.0.1:5000', params))
print(requests.put('http://127.0.0.1:5000/post/3', params))
print(requests.delete('http://127.0.0.1:5000/post/1'))