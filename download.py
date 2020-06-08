import requests
from concurrent.futures import ThreadPoolExecutor
import os
from os.path import getsize

f = open('mp4.txt').read().split(',')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
add_url = 'https://jingcai.cdn-vipkkyun.com/20190912/3504_ae4e7f13/1000k/hls/c105f85f6cf00'


class Download_movie:
    def __init__(self, headers, add_url):
        self.headers = headers
        self.add_url = add_url

    def get_video(self, i):
        with open('ts_files/%s.mp4' % i[-7: -3], 'wb') as f_ts:
            print('开始爬取%s' % i[-7: -3])
            get_ts = requests.get(i)
            f_ts.write(get_ts.content)

    def add_zero_file(self):
        add_list = []
        for root, dirs, files in os.walk('ts_files'):
            for i in files:
                a = getsize('ts_files/' + i)
                if a == 0:
                    add_list.append(self.add_url + i[: -4] + '.ts')
        return add_list

    def writer_in_line(self):
        for root, dirs, files in os.walk('./ts_files'):
            for file in files:
                print(file)
                with open('movie.mp4', 'ab') as f:
                    a = open('./ts_files/' + file, 'rb')
                    f.write(a.read())


conan = Download_movie(headers, add_url)
a = ThreadPoolExecutor(100)
a.map(conan.get_video, f)
