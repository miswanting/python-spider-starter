import json
import time
import os
import urllib.request
from urllib.parse import urlencode
from bs4 import BeautifulSoup


CACHE_FILE_NAME = 'cache.json'
cache = {
    'current_page': 0,
    'nodes': {}
}

url = 'https://www.toli.co.jp/catalog/hinban/hinban.php'
d = 'https://www.toli.co.jp/catalog/download.php'
u = 'https://www.toli.co.jp/catalog/hinban/hinban.php?hinban=20FL1001'


def read_page(num):
    count = num*18
    post_fields = {'hb_next': '次を表示',
                   'count': count,
                   'hinban': '',
                   'hinsyu_code': '',
                   'gara': -1,
                   'color': -1,
                   'from': -1,
                   'to': -1,
                   'kinou1': -1,
                   'kinou2': -1,
                   'kinou3': -1
                   }
    request = urllib.request.Request(url, urlencode(post_fields).encode())
    try:
        raw_html = urllib.request.urlopen(request).read().decode('EUC-JP')
    except urllib.error.URLError as e:
        print(123, e)
    soup = BeautifulSoup(raw_html, "lxml")
    data_list = soup.find(
        id='MAIN').div.table.contents[5].contents[3].form.table.find_all('tr', recursive=False)[1:]
    data = {
        'name': [],
        'img_path': [],
        'link_path': []
    }
    for line in range(3):
        im = data_list[line*2]
        for each in im.find_all('td', recursive=False):
            data['img_path'].append(each.a.img['src'])
            data['link_path'].append(each.a['href'])
            # print(each.a['href'])
            # print(each.a.img['src'])
        te = data_list[line*2+1]
        for each in te.find_all('td', recursive=False):
            data['name'].append(each.table.tr.contents[3].get_text())
            # print(each.table.tr.contents[3].find('a')['href'])
            # print(each.table.tr.contents[3].get_text())
    out = {}
    for i in range(len(data['name'])):
        out.update({
            data['name'][i]: {
                'img': data['img_path'][i],
                'link': data['link_path'][i]
            }
        })
        # out.append({
        #     'name': data['name'][i],
        #     'img': data['img_path'][i],
        #     'link': data['link_path'][i]
        # })
    time.sleep(1)
    return out


if __name__ == "__main__":
    if os.path.exists(CACHE_FILE_NAME):
        with open(CACHE_FILE_NAME) as f:
            cache = json.loads(f.read())
    else:
        with open(CACHE_FILE_NAME, 'w') as f:
            f.write(json.dumps(cache, ensure_ascii=False))
    while True:
        cache['nodes'].update(read_page(cache['current_page']))
        # cache['nodes'].extend()
        print(cache['current_page'], len(cache['nodes']))
        cache['current_page'] += 1
        with open(CACHE_FILE_NAME, 'w') as f:
            f.write(json.dumps(cache))
