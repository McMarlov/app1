import requests
from requests.api import request
params = {"inp_author": "Adic1",
        "inp_quote": "Citata9"}
print(requests.get('http://127.0.0.1:5000'))
#print(requests.put('http://127.0.0.1:5000/post/6', params))
print(requests.delete('http://127.0.0.1:5000/post/8'))