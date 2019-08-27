#!/usr/local/bin/python3

import json
import requests
import wget

number_of_pages = 1
event_id = ''
cookie = 'PHPSESSID='

url = 'https://my.sharingbox.com/public_gallery_get.php' 

headers = {
    'Cookie': cookie
}

data = {
    'idFTPevent': event_id,
    'order': 'undefined',
    'filter': 'undefined',
    'clean': 'undefined',
    'publish': 'undefined',
    'soft_version': '4',
    'dep': '0',
    'count': 'false'
}

print("Getting Photos...")

for page in range(0, number_of_pages):

    print(f"\ndDwnloading pictures on page number {page}")
    data['dep'] = str(page)
    response = requests.post(url, headers=headers, data=data)
    
    picture_list = json.loads(response.text)
    for picture in picture_list['data']:
        file_name = picture['fileN'] + picture['ExtensionFichier']
        wget.download(picture['file'], f"pictures/{file_name}")

print("Done")
