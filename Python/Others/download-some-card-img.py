# coding:utf-8

import urllib
from bs4 import BeautifulSoup
from time import time

def get_content(url):
    """ 获取指定url信息"""
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    return content


def get_second_uri(href_str):
    """通过相对路径获取图片层url"""
    second_uri = href_str.split(">")[1].split("<")[0]
    record = first_uri + second_uri
    return second_uri


def get_file_path(info, before_uri):
    """
     使用BeautifulSoup在网页源码中匹配相应地址
    """
    soup = BeautifulSoup(info)
    # 获取文件夹路径
    paths = soup.find_all("a" )
    second_uri_list = []
    for path in paths:
        second_uri_list.append(before_uri + "/" + get_second_uri(str(path)))
    return second_uri_list[1:]


def download_file(file_name_list):
    """下载文件保持到本地"""
    now = time()
    i = 0
    for file_url in file_name_list:
        for file_ in file_url:
            if file_.endswith("jpg") or file_.endswith("gif") or file_.endswith("png"):
                i = i + 1
                try:
                    print file_
                    urllib.urlretrieve(file_, "{}.{}".format(i, file_[-3:]))
                except:
                    pass
    print "一共下载了　{}张图片, 耗时 {} 秒".format(i, time() - now)


if __name__ == '__main__':
    first_uri = "http://absfx-rf.com/upfile/images"

    info = get_content(first_uri)
    print '获取文件路径中……'
    file_path_list = get_file_path(info, first_uri)
    file_name_list = []
    print '[OK] 获取成功.'
    print ''
    print '获取文件名中……'
    print '[OK] 获取成功.'
    for i in file_path_list:
        info = get_content(i)
        file_name_list.append(get_file_path(info, i))
    print '开始下载文件……'
    download_file(file_name_list)
