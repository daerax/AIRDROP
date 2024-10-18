import requests
txt = {'file': ('acc.txt', open('account1.txt', 'rb'), 'multipart/form-data')}
print(txt)
res = requests.post("http://127.0.0.1:8000/upload/", files=txt)
print(res.status_code)