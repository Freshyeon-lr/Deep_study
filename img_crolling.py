import requests
from lxml.html import parse
from io import StringIO
import urllib.request
import os, sys
from PIL import Image

savedir = "/home/yu/이름 없는 폴더"

def download(URL, filename):
    print('%d image is saving now' % filename)
    name = '%06d' % filename
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(URL, fullname)


keyword = input("검색할 이미지를 입력하세요 : ")
url = 'https://www.google.co.kr/search?q='+keyword+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1002&bih=100' 

#'&hl=ko&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_qfeltuDfAhUBV7wKHdazAugQ_AUIDigB&biw=1855&bih=982'


#'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'


text = requests.get(url, headers={'user-agent': ':Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                               ' Chrome/59.0.3071.115 Safari/537.36'}).text

text_source = StringIO(text)
parsed = parse(text_source)


doc = parsed.getroot()
#imgs = doc.findall('img')
imgs = doc.findall('.//img')

img_list = []
for a in imgs:
    if not a.get('data-src') == None:
        img_list.append(a.get('data-src'))
k = 1
for i in range(len(img_list)):
    download(img_list[i], k)
    k = k +1

#&client=ubuntu&hs=ZDW&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijwNKbmuDfAhVMxbwKHcLzAfAQ_AUIDigB&biw=1855&bih=982#imgrc=_
