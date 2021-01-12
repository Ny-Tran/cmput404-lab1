import requests

print(requests.__version__)

res = requests.get("http://www.google.com")

print(res) 
