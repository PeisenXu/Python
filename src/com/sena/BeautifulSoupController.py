from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

def callbackfunc(blocknum, blocksize, totalsize):

    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''

    percent = 100.0 * blocknum * blocksize / totalsize

    if percent > 100:
        percent = 100

    print("%.2f%%"% percent)
url = 'https://mail.qq.com/cgi-bin/getverifyimage?sid=IMDQi3B0kOipXFgB&r=0.01'
local = 'd:\\total\\logo.jpg'
urlretrieve(url, local, callbackfunc)