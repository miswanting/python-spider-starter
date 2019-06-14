import collections
import json
import os
import threading
import time
import urllib.request
from urllib.parse import urlencode

from bs4 import BeautifulSoup
import SpiderEngine

# CACHE_FILE_NAME = 'cache.json'
# cache = {
#     'current_page': 0,
#     'nodes': {},
#     'task': []
# }
status = {

}
url = 'https://www.toli.co.jp/catalog/hinban/hinban.php'
durl = 'https://www.toli.co.jp/catalog/hinban'
d = 'https://www.toli.co.jp/catalog/download.php'
u = 'https://www.toli.co.jp/catalog/hinban/hinban.php?hinban=20FL1001'


# end = False


# def read_page(num):
#     global e, end
#     count = num*18
#     data = {'hb_next': '次を表示',
#             'count': count,
#             'hinban': '',
#             'hinsyu_code': '',
#             'gara': -1,
#             'color': -1,
#             'from': -1,
#             'to': -1,
#             'kinou1': -1,
#             'kinou2': -1,
#             'kinou3': -1
#             }
#     # request = urllib.request.Request(url, urlencode(data).encode())
#     while True:
#         try:
#             raw_html = e.post(url, data, 'EUC-JP')
#             break
#         except OSError as e:
#             print(123, e)

#     soup = BeautifulSoup(raw_html, "lxml")
#     data_list = soup.find(
#         id='MAIN').div.table.contents[5].contents[3].form.table.find_all('tr', recursive=False)[1:]
#     data = {
#         'name': [],
#         'img_path': [],
#         'link_path': []
#     }
#     for line in range(3):
#         im = data_list[line*2]
#         for each in im.find_all('td', recursive=False):
#             if each.a != None:
#                 data['img_path'].append(each.a.img['src'])
#                 data['link_path'].append(each.a['href'])
#             else:
#                 end = True
#         te = data_list[line*2+1]
#         for each in te.find_all('td', recursive=False):
#             if each.table != None:
#                 data['name'].append(each.table.tr.contents[3].get_text())
#             else:
#                 end = True
#     out = {}
#     for i in range(len(data['name'])):
#         out.update({
#             data['name'][i]: {
#                 'img': data['img_path'][i],
#                 'link': data['link_path'][i]
#             }
#         })
#     time.sleep(1)
#     return out


# def mission_probe():
#     '''获取基本信息'''
#     def task():
#         pass
#     complete = False
#     while not complete:
#         # 产生任务
#         # 运行任务（多线程）
#         cell = read_page(e.data.data['probe_index'])
#         for name in cell:
#             e.new_task({
#                 'name': name,
#                 'img': cell[name]['img'],
#                 'link': cell[name]['link']
#             })
#             # e.data.data['task'].append({
#             #     'name': name,
#             #     'img': cell[name]['img'],
#             #     'link': cell[name]['link']
#             # })
#         e.data.data['nodes'].update(cell)
#         print(e.data.data['probe_index'], len(e.data.data['nodes']))
#         e.data.data['probe_index'] += 1
#         e.save_data()
#     print('probe下载完成！共{}项'.format(len(e.data.data['nodes'])))


# def mission_thumb():
#     '''索引图片下载'''
#     def task():
#         pass
#     complete = False
#     while not complete:
#         if not e.task_is_empty():
#             # if e.data.data['task']:
#             # task = e.data.data['task'].pop()
#             task = e.get_task()
#             print('{}'.format(task['name']))
#             while True:
#                 try:
#                     e.save('t/{}.jpg'.format(task['name']),
#                            e.get(durl+task['img'][1:], encoding='raw'), 'wb')
#                     break
#                 except OSError as er:
#                     print(er)
#             e.finish_task()
#         time.sleep(1)


# def mission_high():
#     '''高清图片下载'''
#     def task():
#         pass
#     complete = False


# def mission_info():
#     '''获取详细信息'''
#     def task():
#         pass
#     complete = False


# def monitor():
#     '''运行状况监控'''
#     print('')


class Project:
    def __init__(self):
        self.data = {
            'done': {
                'probe': False
            },
            'probe_index': 0,
            'nodes': {},
            'task': []

        }
        self.engine = SpiderEngine.Engine()

    def init(self):
        self.engine.config()
        self.engine.init()
        self.data = self.engine.load_data(self.data)
        self.engine.mkdir('t')

    def update(self):
        self.engine.save_data(self.data)

    def start(self):
        p = threading.Thread(target=self.mission_probe)
        p.start()
        t = threading.Thread(target=self.mission_thumb)
        t.start()
        self.monitor()

    def mission_probe(self):
        '''获取基本信息'''
        def task():
            pass
        while not self.data['done']['probe']:
            # 产生任务
            # 运行任务（多线程）
            cell = self.read_page(self.data['probe_index'])
            for name in cell:
                self.engine.new_task({
                    'name': name,
                    'img': cell[name]['img'],
                    'link': cell[name]['link']
                })
                # e.data.data['task'].append({
                #     'name': name,
                #     'img': cell[name]['img'],
                #     'link': cell[name]['link']
                # })
            self.data['nodes'].update(cell)
            # print(self.data['probe_index'], len(
            #     self.data['nodes']))
            self.data['probe_index'] += 1
            self.update()
        print('probe下载完成！共{}项'.format(len(self.data['nodes'])))

    def mission_thumb(self):
        '''索引图片下载'''
        def task():
            pass
        complete = False
        while not complete:
            if not self.engine.task_is_empty():
                # if e.data.data['task']:
                # task = e.data.data['task'].pop()
                task = self.engine.get_task()
                # print('{}'.format(task['name']))
                while True:
                    try:
                        self.engine.save('t/{}.jpg'.format(task['name']),
                                         self.engine.get(durl+task['img'][1:], encoding='raw'), 'wb')
                        break
                    except OSError as er:
                        print(er)
                self.engine.finish_task()
            time.sleep(1)

    def mission_high(self):
        '''高清图片下载'''
        def task():
            pass
        complete = False

    def mission_info(self):
        '''获取详细信息'''
        def task():
            pass
        complete = False

    def monitor(self):
        '''运行状况监控'''
        while True:
            print()
            temp = '{}:{}'
            print(temp.format('PROB', len(self.data['nodes'])))
            print(temp.format('THUM', len(self.data['nodes'])))
            time.sleep(3)

    def read_page(self, num):
        count = num*18
        data = {'hb_next': '次を表示',
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
        # request = urllib.request.Request(url, urlencode(data).encode())
        while True:
            try:
                raw_html = self.engine.post(url, data, 'EUC-JP')
                break
            except OSError as er:
                print(123, er)

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
                if each.a != None:
                    data['img_path'].append(each.a.img['src'])
                    data['link_path'].append(each.a['href'])
                else:
                    self.data['done']['probe'] = True
            te = data_list[line*2+1]
            for each in te.find_all('td', recursive=False):
                if each.table != None:
                    data['name'].append(each.table.tr.contents[3].get_text())
                else:
                    self.data['done']['probe'] = True
        out = {}
        for i in range(len(data['name'])):
            out.update({
                data['name'][i]: {
                    'img': data['img_path'][i],
                    'link': data['link_path'][i]
                }
            })
        time.sleep(1)
        return out


if __name__ == "__main__":
    pro = Project()
    pro.init()
    pro.start()

    # e = SpiderEngine.Engine()
    # e.config()
    # e.init()
    # e.load_data({
    #     'probe_index': 0,
    #     'nodes': {},
    #     'task': []
    # })
    # e.mkdir('t')
    # p = threading.Thread(target=mission_probe)
    # p.start()
    # t = threading.Thread(target=mission_thumb)
    # t.start()
    # monitor()
