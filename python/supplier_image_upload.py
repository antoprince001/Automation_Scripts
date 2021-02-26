
#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path =  'supplier-data/images'
for file in os.listdir(path):
    if '.jpeg' in file:
      dir, name = os.path.split(file)
      filename = os.path.splitext(filename)[0]
      with open(path+filename+'.jpeg', 'rb') as opened:
        r = requests.post(url, files={'file': opened})
