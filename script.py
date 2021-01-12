import requests

print(requests.__version__)

res = requests.get("http://www.google.com")
print(res.status_code)

res = requests.get("https://raw.githubusercontent.com/Ny-Tran/cmput404-lab1/main/script.py")
print(res.text) 
