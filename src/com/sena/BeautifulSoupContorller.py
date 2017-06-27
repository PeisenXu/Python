from urllib.request import urlretrieve


def callbackfunc(blocknum, blocksize, totalsize):
    # 回调函数
    # @blocknum: 已经下载的数据块
    # @blocksize: 数据块的大小
    # @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print("%.2f%%" % percent)


if __name__ == "__main__":
    for i in range(1, 111):
        url = 'https://mail.qq.com/cgi-bin/getverifyimage'
        local = 'd:\\total\\logo' + str(i) + '.jpg'
        urlretrieve(url, local, callbackfunc)
