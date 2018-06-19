# -*- coding: utf-8 -*-

import re
import os
import shutil
import zipfile
import tempfile
import webbrowser
import sys

class Properties(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception as e:
            raise e
        else:
            fopen.close()

    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value

    def put(self, key, value):
        self.properties[key] = value
        replace_property(self.file_name, key + '=.*', key + '=' + value, True)

def parse(file_name):
    return Properties(file_name)

def replace_property(file_name, from_regex, to_str, append_on_not_exists=True):
    tmpfile = tempfile.TemporaryFile()

    if os.path.exists(file_name):
        r_open = open(file_name, 'r')
        pattern = re.compile(r'' + from_regex)
        found = None
        for line in r_open:
            if pattern.search(line) and not line.strip().startswith('#'):
                found = True
                line = re.sub(from_regex, to_str, line)
            tmpfile.write(line)
        if not found and append_on_not_exists:
            tmpfile.write('\n' + to_str)
        r_open.close()
        tmpfile.seek(0)

        content = tmpfile.read()

        if os.path.exists(file_name):
            os.remove(file_name)

        w_open = open(file_name, 'w')
        w_open.write(content)
        w_open.close()

        tmpfile.close()
    else:
        print("file %s not found" % file_name)


class FileUtil(object):
    # 解压指定zip文件
    def Decompression(self, fileName, savePath):
        azip = zipfile.ZipFile(fileName, 'r')
        # 循环解压所有文件
        for file in azip.namelist():
            azip.extract(file, savePath)


    # 获得指定目录里面所有文件
    def file_name(self, file_dir, file_suffix):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.' + file_suffix:
                    L.append(file)
        return L


    def copy_file(self, oldname, newname):
        shutil.copyfile(oldname, newname)


    def excuteCMD(self, cmd):
        p = os.popen(cmd)
        return p


# 打开指定页面
# path为空则使用默认浏览器
# 若找不到应用浏览器，则打开默认浏览器
def openUrl(url, path= None):
    if path:
        chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        if os.path.exists(chromePath):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open(url, new=1, autoraise=True)
        else:
            webbrowser.open(url, new=1, autoraise=True)
    else:
        webbrowser.open(url, new=1, autoraise=True)


    if path == None:
        webbrowser.open(url, new=1, autoraise=True)
    else:
        chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        if os.path.exists(chromePath):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open(url, new=1, autoraise=True)
        else:
            webbrowser.open(url, new=1, autoraise=True)

# 相对路径转绝对路径
# 参数paths: 绝对路径的目录，多参数
# 返回绝对路径
def getAbsPath(*paths):
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    elif __file__:
        dir = os.path.dirname(__file__)
    return os.path.join(dir, *paths)

# 日志记录
def log(context):
    import codecs
    with codecs.open(getAbsPath('log.txt'), 'a', 'gbk') as file:
        file.write(context)
        file.write('\n')