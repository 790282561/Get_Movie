import requests
import re

url = 'https://jingcai.cdn-vipkkyun.com/20190912/3504_ae4e7f13/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
r = requests.get(url+'1000k/hls/index.m3u8', headers=headers)
r_compile = re.compile('\w+.ts')
r2 = re.split(', |\n', r.text)
ts_list = []
for i in r2:
    r3 = r_compile.findall(i)
    if r3 != []:
        ts_list.append(url + '1000k/hls/' + r3[-1])
for j in ts_list:
    with open('mp4.txt', 'a', encoding='UTF-8') as f:
        f.write(j + ',')