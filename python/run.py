#! /usr/bin/env python3

import os
import requests

dpath = 'supplier-data/descriptions/' 
ipath = 'supplier-data/images/'

text_files = sorted(os.listdir(dpath))
jpeg_images = sorted([image_name for image_name in os.listdir(ipath) if '.jpeg' in image_name])

list_content = []
icount = 0

for file in text_files:
    format = ['name','weight','description']

    with open(dpath + file, 'r') as fi:
        data = {}
        contents = f.read().split("\n")[0:3]

        contents[1] = int((re.search(r'\d+', contents[1])).group())

        counter =0
        for content in contents:
            data[format[counter]] = content
            counter+=1

        data['image_name'] = jpeg_images[icount]

        list_content.append(data)
        icount += 1

for item in list_content:
    resp = requests.post('http://127.0.0.1:80/fruits/', json=item)
    if resp.status_code != 201: 
        raise Exception('POST error status={}'.format(resp.status_code))
